"""Application paths and defaults."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_TASKS_FILE = PROJECT_ROOT / "data" / "tasks.json"

USAGE = """Usage:
  python toolkit.py summary
  python toolkit.py points [status]
  python toolkit.py load [assignee]
  python toolkit.py tag <name>

Commands:
  summary          Show task counts by status and total story points
  points [status]  Sum story points (optionally filtered by status)
  load [assignee]  Show open story points per assignee (or one assignee)
  tag <name>       List tasks matching a tag (case-insensitive)
"""
