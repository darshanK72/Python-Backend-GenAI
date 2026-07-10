# Assignment 01 — Data Toolkit CLI

MAS prerequisite foundation assignment. Standard library only (plus pytest for tests).

Problem statement: [`data_toolkit_assignment.md`](data_toolkit_assignment.md)

## Project layout

```
01_data_toolkit_cli/
  app/
    main.py                 # Entry point: python -m app.main
    config.py               # Paths and CLI usage text
    services/
      analytics.py          # Importable analytics functions
    cli/
      commands.py           # Command output handlers
      runner.py             # Argument dispatch and exit codes
  data/
    tasks.json              # Sample sprint data (12 tasks)
  toolkit.py                # Assignment shim: python toolkit.py <command>
  tests/
    conftest.py
    services/test_analytics.py
    cli/test_commands.py
    cli/test_runner.py
    app/test_config.py
    integration/test_cli_e2e.py
  requirements.txt
```

## Setup

```bash
cd "00. Notes & Documents/MAS_Foundation_Assignments/01_data_toolkit_cli"
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run commands

Either entry point works:

```bash
python toolkit.py summary
python -m app.main summary
```

Example output:

```
Task summary
--------------------------------
  blocked        2
  done           3
  in_progress    3
  todo           4
--------------------------------
  total points   63
  open points    44
```

```bash
python toolkit.py points
python toolkit.py points done
python toolkit.py load
python toolkit.py load Bob
python toolkit.py tag auth
```

## Tests

```bash
pytest tests/ -v
```

No network access required.
