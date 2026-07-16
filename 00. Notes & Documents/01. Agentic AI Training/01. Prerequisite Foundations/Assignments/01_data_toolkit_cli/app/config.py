"""Application paths and defaults."""

from pathlib import Path

# PROJECT_ROOT - the root directory of the project
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# DEFAULT_TASKS_FILE - the default tasks file
DEFAULT_TASKS_FILE = PROJECT_ROOT / "data" / "tasks.json"

# VALID_COMMANDS - the valid commands for the data toolkit CLI
VALID_COMMANDS = ("summary", "points", "load", "tag")

# HELP_TEXT - the help text for the data toolkit CLI
HELP_TEXT = """\
Usage: python toolkit.py <command> [args]

Commands:
  summary              Show task counts by status and total story points
  points [status]      Sum story points (optionally: todo, in_progress, done, blocked)
  load [assignee]      Show open story points per assignee (or one assignee)
  tag <name>           List tasks matching a tag (case-insensitive)

Examples:
  python toolkit.py summary
  python toolkit.py points done
  python toolkit.py load Alice
  python toolkit.py tag auth
"""
