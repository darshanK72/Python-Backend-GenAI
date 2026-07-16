# Assignment 01 — Data Toolkit CLI

**Track:** Python Foundations · **Difficulty:** Medium · **Marks:** 10 · **Est. time:** ~2.5 hrs

A command-line toolkit that loads sprint task data from JSON and answers common analytics questions — counts by status, story-point totals, assignee load, and tag filtering. Business logic lives in an importable service module; the CLI is a thin dispatcher with clear error messages and non-zero exit codes on failure.

**Problem statement:** `[data_toolkit_assignment.md](data_toolkit_assignment.md)`

---

## Overview

An engineering team keeps sprint data in a JSON file exported from a planning tool. This CLI loads that file, validates it, and exposes four commands for quick analysis.

### What you will practice

- Python modules and package layout
- Type-hinted functions with docstrings
- JSON I/O and custom error handling
- Manual `sys.argv` CLI dispatch with usage messages
- `pytest` unit and integration tests



### Tech stack


| Component      | Choice                |
| -------------- | --------------------- |
| Language       | Python 3.10+          |
| Runtime deps   | Standard library only |
| Test framework | pytest                |


---



## Quick start

From the assignment directory:

```bash
cd "01. Prerequisite Foundations/Assignments/01_data_toolkit_cli"
python toolkit.py summary
```

Install test dependencies from the **repository root** (shared venv) or locally:

```bash
pip install -r requirements.txt
pytest tests/ -v
```

No `.env` file is required — runtime code uses only the standard library.

---

## Architecture

```text
toolkit.py                 # CLI entry point (calls runner.main)
    └── app/cli/runner.py  # Argument parsing, dispatch, exit codes
            ├── app/cli/commands.py   # Formatted stdout for each command
            └── app/services/analytics.py  # Importable analytics functions
```


| Module                      | Responsibility                                                               |
| --------------------------- | ---------------------------------------------------------------------------- |
| `toolkit.py`                | Thin shim so the CLI can be run as `python toolkit.py <command>`             |
| `app/config.py`             | Project paths, valid commands, and help text                                 |
| `app/cli/runner.py`         | Reads arguments, loads tasks, routes to command handlers, returns exit codes |
| `app/cli/commands.py`       | Prints human-readable output for `summary`, `points`, `load`, and `tag`      |
| `app/services/analytics.py` | Core data loading and analytics (importable, testable without the CLI)       |


`runner.main()` accepts an optional `argv` list so tests can invoke the CLI without spawning a subprocess.

---



## Project structure

```text
01_data_toolkit_cli/
├── app/
│   ├── config.py               # Paths, valid commands, help text
│   ├── cli/
│   │   ├── commands.py         # Command output handlers
│   │   └── runner.py           # Argument dispatch and exit codes
│   └── services/
│       └── analytics.py        # Importable analytics functions
├── data/
│   └── tasks.json              # Sample sprint data (12 tasks)
├── tests/
│   ├── conftest.py             # Shared fixtures
│   ├── services/test_analytics.py
│   ├── cli/test_commands.py
│   ├── cli/test_runner.py
│   └── integration/test_cli_e2e.py
├── toolkit.py                  # Entry point: python toolkit.py <command>
├── data_toolkit_assignment.md
├── pytest.ini
├── requirements.txt            # pytest only
└── README.md
```

---



## Setup



### Option A — repository root (recommended)

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux
pip install -r requirements.txt
```

Then run tests from the assignment folder:

```bash
cd "01. Prerequisite Foundations/Assignments/01_data_toolkit_cli"
pytest tests/ -v
```



### Option B — assignment-only venv

```bash
cd "01. Prerequisite Foundations/Assignments/01_data_toolkit_cli"
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux
pip install -r requirements.txt
```

---



## Data model

`data/tasks.json` contains a JSON array of **12** task objects:


| Field          | Type      | Notes                                       |
| -------------- | --------- | ------------------------------------------- |
| `id`           | int       | Unique task identifier                      |
| `title`        | str       | Task title                                  |
| `assignee`     | str       | Person responsible                          |
| `story_points` | int       | Effort estimate                             |
| `status`       | str       | `todo` · `in_progress` · `done` · `blocked` |
| `tags`         | list[str] | Labels attached to the task                 |


---



## Analytics module

All analytics live in `app/services/analytics.py`:


| Symbol            | Signature / type                                        | Description                                                       |
| ----------------- | ------------------------------------------------------- | ----------------------------------------------------------------- |
| `TaskDataError`   | `Exception`                                             | Raised when the task file is missing, unreadable, or invalid      |
| `load_tasks`      | `(path: str) -> list[dict]`                             | Reads and parses JSON; raises `TaskDataError` on failure          |
| `count_by_status` | `(tasks: list[dict]) -> dict[str, int]`                 | Counts tasks per status                                           |
| `total_points`    | `(tasks: list[dict], status: str \| None = None) -> int` | Sums `story_points` (optionally filtered by status)               |
| `assignee_load`   | `(tasks: list[dict]) -> dict[str, int]`                 | Open (non-`done`) story points per assignee, sorted highest first |
| `filter_by_tag`   | `(tasks: list[dict], tag: str) -> list[dict]`           | Tasks whose `tags` contain the given tag (case-insensitive)       |


---



## CLI reference

```bash
python toolkit.py <command> [args]
```


| Command   | Arguments    | Description                                          |
| --------- | ------------ | ---------------------------------------------------- |
| `summary` | —            | Task counts by status, total points, and open points |
| `points`  | `[status]`   | Sum story points (optionally filtered by status)     |
| `load`    | `[assignee]` | Open story points per assignee (or one assignee)     |
| `tag`     | `<name>`     | List tasks matching a tag (**required** argument)    |




### Help

```bash
python toolkit.py --help
python toolkit.py -h
python toolkit.py help
```

Help prints to **stdout** and exits `0`. Running with no command prints the same usage text to **stderr** and exits `1`.

### Example invocations

**Summary** — counts and totals across all tasks:

```bash
python toolkit.py summary
```

```text
Task summary
--------------------------------
  blocked        2
  done           3
  in_progress    3
  todo           4
--------------------------------
  total points  63
  open points   44
```

**Points** — all tasks or filtered by status:

```bash
python toolkit.py points
python toolkit.py points done
```

```text
Total story points: 63
Story points (done): 19
```

**Load** — open points per assignee or for one person:

```bash
python toolkit.py load
python toolkit.py load Bob
```

```text
Open story points by assignee
--------------------------------
  Bob           16
  Alice         10
  Carol          8
  Dana           8
  Eve            2
Open story points for Bob: 16
```

**Tag** — find tasks by label:

```bash
python toolkit.py tag auth
```

```text
Tasks tagged 'auth' (2)
------------------------------------------------
  # 2 [in_progress] Design login screen (Bob)
  # 3 [todo] Implement password reset (Bob)
```

---



## Error handling


| Condition                  | Behavior                                                                              | Exit code |
| -------------------------- | ------------------------------------------------------------------------------------- | --------- |
| No command given           | Prints usage to stderr                                                                | `1`       |
| `--help`, `-h`, or `help`  | Prints usage to stdout                                                                | `0`       |
| Unknown command            | `toolkit.py: '<cmd>' is not a toolkit command.` + similar-command suggestions + usage | `1`       |
| `tag` without name         | `Error: 'tag' requires a tag name.` + usage                                           | `1`       |
| Missing tasks file         | `Error: Task file not found: ...`                                                     | `1`       |
| Invalid JSON / wrong shape | `Error: ...` (clear message, no traceback)                                            | `1`       |
| Success                    | Human-readable stdout                                                                 | `0`       |


Output is always **human-readable text**, never a raw Python dict dump.

---



## Tests

```bash
pytest tests/ -v
```


| Test file                           | Coverage                                            |
| ----------------------------------- | --------------------------------------------------- |
| `tests/services/test_analytics.py`  | Each analytics function, including error cases      |
| `tests/cli/test_commands.py`        | Formatted output for all four commands              |
| `tests/cli/test_runner.py`          | Argument dispatch, help, and exit codes             |
| `tests/integration/test_cli_e2e.py` | End-to-end runs against committed `data/tasks.json` |


No network access or mocking required.

---



## Submission checklist

- [ ] `tasks.json` with at least 12 tasks committed
- [ ] Importable `analytics` module separate from CLI entry point
- [ ] All five functions type-hinted with one-line docstrings
- [ ] pytest tests covering each function and at least one error case
- [ ] README with example invocations and output for all four commands

**Foundation pass criteria:** 30/50 overall, with at least **12/30** across Assignments 01–03.