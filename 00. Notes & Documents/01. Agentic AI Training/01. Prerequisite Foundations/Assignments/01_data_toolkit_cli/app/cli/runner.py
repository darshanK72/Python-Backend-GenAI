"""CLI argument parsing and command dispatch."""

from __future__ import annotations

import sys
from pathlib import Path

from app.cli.commands import cmd_load, cmd_points, cmd_summary, cmd_tag
from app.config import DEFAULT_TASKS_FILE, USAGE
from app.services.analytics import TaskDataError, load_tasks


def load_default_tasks(tasks_file: Path | None = None) -> list[dict]:
    """Load tasks from the default data file or a provided path."""
    path = tasks_file or DEFAULT_TASKS_FILE
    return load_tasks(str(path))


def main(argv: list[str] | None = None, *, tasks_file: Path | None = None) -> int:
    """Run the data toolkit CLI and return an exit code."""
    args = list(sys.argv[1:] if argv is None else argv)
    if not args:
        print(USAGE, file=sys.stderr)
        return 1

    command = args[0].lower()

    try:
        tasks = load_default_tasks(tasks_file)
    except TaskDataError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if command == "summary":
        cmd_summary(tasks)
        return 0

    if command == "points":
        cmd_points(tasks, args[1] if len(args) > 1 else None)
        return 0

    if command == "load":
        cmd_load(tasks, args[1] if len(args) > 1 else None)
        return 0

    if command == "tag":
        if len(args) < 2:
            print("Error: 'tag' requires a tag name.", file=sys.stderr)
            print(USAGE, file=sys.stderr)
            return 1
        cmd_tag(tasks, args[1])
        return 0

    print(f"Error: unknown command '{command}'.", file=sys.stderr)
    print(USAGE, file=sys.stderr)
    return 1
