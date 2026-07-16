# Assignment 04 — Prompt Engineering Toolkit

**Track:** Generative AI Basics · **Difficulty:** Medium · **Marks:** 10 · **Est. time:** ~2.5 hrs

A CLI toolkit that extracts structured fields from messy bug reports using three prompting strategies — naive, structured, and few-shot — and compares reliability against token cost. This is the single most transferable GenAI skill into the MAS program.

**Problem statement:** [`prompt_engineering_assignment.md`](prompt_engineering_assignment.md)

---

## Overview

Before building agents, engineers need to understand how prompt wording changes model behaviour and how to get reliable, machine-parseable output. This project runs the **same extraction task** three different ways over a shared dataset, reports token usage per call, and documents which strategy works best.

### What you will practice

- OpenAI chat-completions API (system/user messages)
- Prompt engineering: role, schema, few-shot examples
- Structured JSON output parsing with corrective retry
- Token awareness (`usage` field, running totals)
- `temperature=0` for deterministic extraction

### Tech stack

| Component | Choice |
|-----------|--------|
| LLM API | OpenAI (or compatible) |
| Config | python-dotenv + pydantic-settings |
| Tests | pytest (mocked LLM client) |

---

## Project structure

```
04_prompt_engineering_toolkit/
├── prompt_toolkit.py              # CLI entry shim: python prompt_toolkit.py
├── data/
│   └── reports.json               # 5 committed bug reports
├── app/
│   ├── config.py                  # Paths, help text, and .env loading
│   ├── cli/
│   │   ├── commands.py            # Run-all-strategies command handler
│   │   ├── runner.py              # Argument dispatch and exit codes
│   │   └── output.py              # Formatted console output
│   ├── services/
│   │   ├── llm_service.py         # OpenAI client wrapper
│   │   ├── json_parser.py         # JSON extraction + retry
│   │   ├── token_tracker.py       # Running token totals
│   │   └── report_loader.py       # Load reports.json
│   ├── strategies/
│   │   └── extraction.py          # naive / structured / few-shot
│   └── schemas/
│       └── extraction.py          # Output field definitions
├── tests/
├── .env.example
├── prompt_engineering_assignment.md
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Prerequisites

- Python 3.10+
- OpenAI API key with billing/credits configured
- Set a small spending limit before running live calls

---

## Setup

```bash
cd "01. Prerequisite Foundations/Assignments/04_prompt_engineering_toolkit"
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux
pip install -r requirements.txt
copy .env.example .env          # Windows
# cp .env.example .env          # macOS / Linux
```

Edit `.env`:

```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4o-mini
```

**Never commit `.env`** — load keys from environment only.

---

## Configuration

Environment variables are loaded from **this assignment's** `.env` file only (`04_prompt_engineering_toolkit/.env`). Copy `.env.example` to `.env` in the assignment folder before live runs.

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `OPENAI_API_KEY` | Yes (live runs) | — | OpenAI API key |
| `OPENAI_MODEL` | No | `gpt-4o-mini` | Model for extraction calls |
| `extraction_temperature` | — | `0.0` (hardcoded) | Set to 0 for deterministic parsing |

---

## Run

```bash
python prompt_toolkit.py
```

This runs all three strategies over every report in `data/reports.json` and prints:

- Strategy name and report index
- Extracted result (or failure message)
- Per-call token usage: `tokens: prompt={n}, completion={m}, running_total={total}`
- Final summary: `Total tokens used: {running_total}`

Exit code `0` on success, `1` if `reports.json` is missing or has fewer than 5 reports.

### Importable functions

```python
from app.strategies.extraction import naive_extract, structured_extract, fewshot_extract

result_str = naive_extract("the app crashes when I hit save...")
result_dict = structured_extract("the app crashes when I hit save...")
result_dict = fewshot_extract("the app crashes when I hit save...")
```

---

## The extraction task

Given a free-text bug report, extract:

```json
{
  "summary": "string",
  "component": "string",
  "severity": "low|medium|high|critical",
  "reproducible": true
}
```

**Example input:**

```
the app crashes when I hit save on the settings page on my iphone, super urgent, happens every time
```

**Example structured output:**

```json
{
  "summary": "App crashes on save in settings",
  "component": "settings",
  "severity": "critical",
  "reproducible": true
}
```

---

## Three prompting strategies

| Function | Return type | Approach |
|----------|-------------|----------|
| `naive_extract(report)` | `str` | Minimal one-line prompt — returns unstructured prose |
| `structured_extract(report)` | `dict` | System role + explicit field definitions + JSON-only instruction |
| `fewshot_extract(report)` | `dict` | Structured prompt + 2–3 worked input→JSON examples |

### Naive prompt

Single user message:

> Extract summary, component, severity, and reproducible from: {report}

### Structured prompt

System message defines role, required JSON keys, allowed severity values (`low` / `medium` / `high` / `critical`), and `reproducible` as boolean. User message wraps the report.

### Few-shot prompt

Same system prompt as structured, plus 3 example exchanges (user report → assistant JSON) before the target report.

---

## Temperature choice

All extraction calls use **`temperature=0`**.

Field extraction is a **deterministic parsing task**, not creative writing. Low temperature reduces randomness so `severity` and boolean fields stay consistent across runs and strategies can be compared fairly.

---

## JSON retry behaviour

`structured_extract` and `fewshot_extract` handle malformed model output:

1. Parse response with `extract_json_block()` (strips optional ` ```json ` fences)
2. On `JSONDecodeError` → append assistant message + corrective instruction → **one retry**
3. Still invalid → `StructuredParseError` reported cleanly (CLI prints `Failed: ...`, run continues)
4. **Never crashes** the full toolkit run

`naive_extract` returns raw text — no JSON parsing or retry.

---

## Token reporting

`TokenTracker` accumulates usage across all LLM calls:

```
tokens: prompt=142, completion=38, running_total=180
...
Total tokens used: 1247
```

Token counts come from the API response `usage` field (`prompt_tokens` + `completion_tokens`).

---

## Strategy comparison (reliability vs token cost)

| Strategy | Structured JSON reliability | Typical token cost |
|----------|----------------------------|--------------------|
| **Naive** | Low — often returns prose or mixed formats | Lowest per call (short prompt) |
| **Structured** | High — explicit schema + JSON-only instruction | Medium |
| **Few-shot** | Highest — examples anchor format and severity mapping | Highest (longer prompt) |

Across the 5 committed reports:

- **Few-shot** produces valid JSON with correct `severity` most reliably, especially for ambiguous feedback vs bug language
- **Structured** is a strong second with lower token cost
- **Naive** is cheapest but least reliable for machine parsing

Re-run `python prompt_toolkit.py` and compare the printed `running_total` for exact token spend with your API key and model.

---

## Sample reports

`data/reports.json` contains 5 bug reports covering crashes, UI issues, performance problems, feature-like language, and urgent reproducible defects. All three strategies run over the same inputs for fair comparison.

---

## Error handling

| Condition | Behaviour |
|-----------|-----------|
| Missing `reports.json` | Exit code `1`, stderr error message |
| Fewer than 5 reports in file | Exit code `1` |
| Missing `OPENAI_API_KEY` | `RuntimeError` with clear message |
| JSON parse fails after 1 retry | `Failed: Could not parse structured JSON after retry: ...` |
| Success | Exit code `0` |

---

## Tests

```bash
pytest tests/ -v
```

OpenAI client is **mocked** — no live API calls or key required. Tests cover:

- Token tracking and running totals
- JSON parser (including markdown fences)
- Strategy message builders
- Structured retry logic
- CLI runner output and exit codes
- Report loader validation

---

## Submission checklist

- [ ] Three strategy functions with visibly distinct prompts
- [ ] API key loaded from `.env` (never committed); `.env.example` present
- [ ] JSON-parse error handling with one corrective retry
- [ ] Token usage printed per call with a running total
- [ ] `reports.json` with 5+ samples and README comparison of reliability vs token cost

**Foundation pass criteria:** 30/50 overall, with at least **8/20** across Assignments 04–05.
