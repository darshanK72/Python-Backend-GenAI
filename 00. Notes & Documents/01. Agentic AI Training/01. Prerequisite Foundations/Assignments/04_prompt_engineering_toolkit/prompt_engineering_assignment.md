# Assignment 04 — Prompt Engineering Toolkit

**Source:** MAS_TRAINING-000_Prerequisite_Foundations  
**Track:** Generative AI Basics  
**Difficulty:** Medium  
**Marks:** 10  
**Estimated time:** ~2.5 hours  
**Required stack:** Python · OpenAI (or equiv) API · python-dotenv

---

## Pattern

GenAI basics — LLM API calls, prompt principles, structured JSON output, token awareness.

---

## Scenario

Before building agents, engineers need to feel how prompt wording changes model behaviour and how to get reliable, machine-parseable output. You are building a small toolkit that runs the same task three ways — naive, structured, and few-shot — over a set of inputs, and reports both the results and the token cost. This is the single most transferable skill into the MAS program.

---

## What You Need to Build

A Python script, `prompt_toolkit.py`, that performs one concrete task — extracting structured fields from messy free-text bug reports — using three prompting strategies, and compares them. The API key is loaded from a `.env` file.

### The task

Given a free-text bug report (e.g. “the app crashes when I hit save on the settings page on my iphone, super urgent, happens every time”), extract a structured record:

```json
{
  "summary": "string",
  "component": "string",
  "severity": "low|medium|high|critical",
  "reproducible": true
}
```

### Three strategies (each its own function)

| Function | Return type | Description |
|----------|-------------|-------------|
| `naive_extract(report: str)` | `str` | A minimal one-line prompt. Returns whatever the model says (likely unstructured). |
| `structured_extract(report: str)` | `dict` | A prompt with a clear role, explicit field definitions, allowed severity values, and an instruction to return only JSON. Parses the JSON into a dict. |
| `fewshot_extract(report: str)` | `dict` | Builds on the structured prompt by adding 2–3 worked examples (input report → ideal JSON) before the real input. Parses to a dict. |

### Behaviours & constraints

- **Inputs:** Run all three strategies over the same set of at least **5** sample reports committed in a `reports.json` file.
- **JSON robustness:** `structured_extract` and `fewshot_extract` must handle the case where the model returns slightly malformed JSON — catch the parse error and retry once with a corrective instruction, or report the failure cleanly. **Never crash.**
- **Token reporting:** For each call, print the prompt and completion token counts from the API response `usage` field, and a **running total**.
- **Parameters:** Use `temperature=0` for the extraction calls and explain in the README why low temperature suits this task.
- **Comparison:** Produce a short comparison in the README: which strategy produced valid structured output most reliably across the 5 reports, and at what token cost.

---

## Milestones

| Phase | What you're building | Time |
|-------|----------------------|------|
| **M1 — API Setup & Data** | Load the key from `.env`, make a first successful call, and commit `reports.json` with 5+ sample reports. | 25 min |
| **M2 — Three Strategies** | Implement the naive, structured, and few-shot extraction functions with their distinct prompts. | 50 min |
| **M3 — Robust Parsing & Tokens** | Add JSON-parse error handling with one corrective retry; print token usage and a running total. | 35 min |
| **M4 — Comparison & Docs** | Run all strategies over the 5 reports; write the README comparison of reliability vs token cost. | 30 min |

---

## Marking Rubric (10 marks)

Each criterion is worth **2 marks**.

| # | Criterion | 2 marks — Full | 1 mark — Partial | 0 marks — Missing |
|---|-----------|----------------|------------------|-------------------|
| 1 | **Structure & Correctness** | Three distinct strategy functions; key loaded from `.env`; calls succeed; JSON parsed into dicts | Strategies present but two prompts nearly identical, or key hardcoded (–1) | Calls fail; no working strategies; or only one strategy |
| 2 | **Core Functionality (Prompting)** | Structured and few-shot prompts use role, explicit fields, allowed values, and (few-shot) worked examples; produce valid structured output | Prompts work but lack explicit field/value constraints, or few-shot has no real examples | Prompts produce unstructured output; no real prompt engineering |
| 3 | **Robustness (JSON + tokens)** | Malformed JSON caught with a corrective retry; never crashes; token usage printed with running total | Handles JSON or tokens but not both; one crash path remains | No JSON error handling; crashes on bad output; no token reporting |
| 4 | **End-to-End Run** | All three strategies run over all 5 reports and produce the documented comparison | Runs over most inputs; comparison thin or missing one strategy | Crashes or only runs on one input |
| 5 | **Documentation** | README explains temperature choice + strategy comparison (reliability vs token cost); `reports.json` committed | Runs; README missing comparison or temperature rationale | No README; no sample data |

---

## Submission Checklist

- [ ] Three strategy functions with visibly distinct prompts
- [ ] API key loaded from `.env` (never committed); `.env.example` present
- [ ] JSON-parse error handling with one corrective retry
- [ ] Token usage printed per call with a running total
- [ ] `reports.json` with 5+ samples and a README comparison of reliability vs token cost

---

## Pass context (foundation course)

Foundation pass criteria: **30/50 overall**, with at least **8/20** across Assignments 04–05.
