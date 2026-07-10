# Assignment 04 — Prompt Engineering Toolkit

Compare naive, structured, and few-shot prompting for extracting fields from bug reports.

**Problem statement:** [prompt_engineering_assignment.md](prompt_engineering_assignment.md)

## Project layout

```
04_prompt_engineering_toolkit/
├── prompt_engineering_assignment.md
├── prompt_toolkit.py              # CLI entry shim
├── data/reports.json              # 5 committed bug reports
├── app/
│   ├── main.py                    # exports strategy entry points
│   ├── config.py
│   ├── cli/runner.py              # runs all strategies
│   ├── services/                  # LLM client, JSON parser, token tracker
│   ├── strategies/extraction.py   # naive / structured / few-shot endpoints
│   └── schemas/extraction.py
└── tests/
```

## Setup

```bash
cd "00. Notes & Documents/MAS_Foundation_Assignments/04_prompt_engineering_toolkit"
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
# Add your OpenAI API key
```

## Run

```bash
python prompt_toolkit.py
```

Runs all three strategies over the 5 reports in `data/reports.json` and prints token usage after each LLM call.

## Strategy entry points

| Function | Return | Description |
|----------|--------|-------------|
| `naive_extract(report)` | `str` | Minimal one-line prompt |
| `structured_extract(report)` | `dict` | Role + schema + JSON-only instructions |
| `fewshot_extract(report)` | `dict` | Structured prompt + 3 worked examples |

Import from `app.main` or `app.strategies.extraction`.

## Tests

```bash
pytest tests/ -v
```

Tests mock the OpenAI client — no live API calls required.

## Temperature choice

All extraction calls use `temperature=0` because field extraction is a **deterministic parsing task**, not a creative writing task. Lower temperature reduces randomness so severity and boolean fields stay consistent across runs.

## Strategy comparison (reliability vs token cost)

| Strategy | Structured JSON reliability | Typical token cost |
|----------|----------------------------|--------------------|
| Naive | Low — often returns prose or mixed formats | Lowest per call (short prompt) |
| Structured | High — explicit schema + JSON-only instruction | Medium |
| Few-shot | Highest — examples anchor format and severity mapping | Highest (longer prompt) |

Across the 5 committed reports, **few-shot** usually produces valid JSON with correct `severity` values most reliably, especially for ambiguous feedback vs bug language. **Structured** is a strong second with lower token cost. **Naive** is cheapest but least reliable for machine parsing.

Re-run `prompt_toolkit.py` and compare the printed `running_total` to see exact token spend for your API key and model.

## Output schema

Each structured/few-shot extraction targets:

```json
{
  "summary": "string",
  "component": "string",
  "severity": "low|medium|high|critical",
  "reproducible": true
}
```

Malformed JSON triggers one corrective retry before reporting failure cleanly.
