# Assignment 01 — Data Toolkit CLI

**Source:** MAS_TRAINING-000_Prerequisite_Foundations  
**Track:** Python Foundations  
**Difficulty:** Medium  
**Marks:** 10  
**Estimated time:** ~2.5 hours  
**Required stack:** Python 3.10+ · standard library · pytest

---

## Pattern

Python Foundations — modules, typed functions, error handling, JSON I/O, unit tests.

---

## Scenario

An engineering team keeps its sprint data in a messy JSON file exported from a planning tool. Analysts waste time hand-counting tasks and recomputing totals. You are building a small command-line toolkit that loads the file, validates it, and answers a handful of common questions — the kind of reliable, typed, tested utility every engineer should be able to produce before touching agents.

---

## What You Need to Build

A CLI script, `toolkit.py`, plus a `tasks.json` data file, organised into a small package with at least one importable module (e.g. `analytics.py`) that `toolkit.py` calls.

### Input data

Commit a `tasks.json` containing a list of **at least 12** task objects. Each task has:

| Field | Type | Notes |
|-------|------|-------|
| `id` | int | Unique task identifier |
| `title` | str | Task title |
| `assignee` | str | Person responsible |
| `story_points` | int | Effort estimate |
| `status` | str | One of `'todo'` / `'in_progress'` / `'done'` / `'blocked'` |
| `tags` | list[str] | Labels attached to the task |

### Functions (in the importable module, all type-hinted)

| Function | Signature | Description |
|----------|-----------|-------------|
| `load_tasks` | `(path: str) -> list[dict]` | Reads and parses the JSON file. Raises a clear, custom error message if the file is missing or the JSON is malformed. |
| `count_by_status` | `(tasks: list[dict]) -> dict[str, int]` | Returns a count of tasks per status, e.g. `{'todo': 4, 'done': 5, ...}`. |
| `total_points` | `(tasks: list[dict], status: str \| None = None) -> int` | Sums `story_points` across all tasks, or only those matching `status` when provided. |
| `assignee_load` | `(tasks: list[dict]) -> dict[str, int]` | Returns total **open** (non-done) story points per assignee, sorted highest first. |
| `filter_by_tag` | `(tasks: list[dict], tag: str) -> list[dict]` | Returns every task whose `tags` list contains the given tag (**case-insensitive**). |

### CLI behaviour

Invoked as:

```bash
python toolkit.py <command> [args]
```

| Command | Args | Description |
|---------|------|-------------|
| `summary` | — | Show task counts by status and totals |
| `points` | `[status]` | Sum story points (optionally filtered by status) |
| `load` | `[assignee]` | Show open story points per assignee (or one assignee) |
| `tag` | `<name>` | List tasks matching a tag |

**Requirements:**

- Unknown command or missing required argument prints a **helpful usage message** and exits with a **non-zero status code** — it does not crash with a traceback.
- Output is **human-readable text**, not a raw dict dump.

### Constraints

- Every public function has **type hints** and a **one-line docstring**.
- All file and parsing errors are caught and reported as **clear messages**.
- **No third-party packages** — standard library only (`argparse` or `sys.argv` is fine).  
  *(pytest is the only allowed dependency, for tests.)*

---

## Milestones

| Phase | What you're building | Time |
|-------|----------------------|------|
| **M1 — Project & Data Setup** | Create the package layout, the `tasks.json` fixture, and the virtual environment with a `requirements.txt` (pytest only). | 20 min |
| **M2 — Core Functions** | Implement the five typed analytics functions in the importable module with docstrings. | 45 min |
| **M3 — CLI & Error Handling** | Wire the command dispatcher, usage messages, and exit codes; catch all file/JSON errors. | 40 min |
| **M4 — Testing & Docs** | Write pytest tests for each function (including an error case); README with run examples for all four commands. | 30 min |

---

## Marking Rubric (10 marks)

Each criterion is worth **2 marks**.

| # | Criterion | 2 marks — Full | 1 mark — Partial | 0 marks — Missing |
|---|-----------|----------------|------------------|-------------------|
| 1 | **Structure & Correctness** | Code split into an importable module + CLI; all functions type-hinted with docstrings; logic correct | Works but everything in one file, or type hints/docstrings largely missing | Functions absent or return wrong values; no module structure |
| 2 | **Core Functionality** | All five functions return correct results across the sample data and evaluator inputs | 3–4 functions correct; one returns wrong counts/totals | Most functions broken or missing |
| 3 | **Error Handling & Robustness** | Missing file, bad JSON, unknown command, and missing args all produce clear messages and non-zero exit — no tracebacks | Some errors handled; at least one path crashes with a raw traceback | No error handling; crashes on any bad input |
| 4 | **End-to-End Run** | All four CLI commands run correctly on the committed data and evaluator data | 3 of 4 commands correct; one wrong or errors | Crashes or wrong output on sample |
| 5 | **Documentation** | README with run examples for every command; `tasks.json` committed; pytest tests pass | Code runs; README missing examples or some tests absent | No README; no tests; no sample data |

---

## Submission Checklist

- [ ] `tasks.json` with at least 12 tasks committed
- [ ] Importable analytics module separate from the CLI entry point
- [ ] pytest tests covering each function and at least one error case
- [ ] README with example invocations and output for all four commands

---

## Pass context (foundation course)

Foundation pass criteria: **30/50 overall**, with at least **12/30** across Assignments 01–03.
