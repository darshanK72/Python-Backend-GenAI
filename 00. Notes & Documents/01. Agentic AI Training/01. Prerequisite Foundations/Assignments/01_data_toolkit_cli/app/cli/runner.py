"""CLI argument parsing and command dispatch."""

from __future__ import annotations

import difflib
import sys
from pathlib import Path

from app.cli.commands import cmd_load, cmd_points, cmd_summary, cmd_tag
from app.config import DEFAULT_TASKS_FILE, HELP_TEXT, VALID_COMMANDS
from app.services.analytics import TaskDataError, load_tasks


# load_default_tasks - load tasks from the default data file or a provided path
def load_default_tasks(tasks_file: Path | None = None) -> list[dict]:
    """Load tasks from the default data file or a provided path."""
    path = tasks_file or DEFAULT_TASKS_FILE
    return load_tasks(str(path))

# _print_help - print the help text
def _print_help(*, stream: object = sys.stderr) -> None:
    print(HELP_TEXT, file=stream, end="")

# _unknown_command_message - print the unknown command message
def _unknown_command_message(command: str) -> str:
    lines = [f"toolkit.py: '{command}' is not a toolkit command."]
    suggestions = difflib.get_close_matches(command, VALID_COMMANDS, n=3, cutoff=0.5)
    if suggestions:
        lines.append("")
        lines.append("The most similar commands are")
        lines.extend(f"\t{name}" for name in suggestions)
    return "\n".join(lines)

# _print_error_with_help - print the error message with the help text
def _print_error_with_help(message: str) -> None:
    print(f"{message}\n\n{HELP_TEXT}", file=sys.stderr, end="")

# main - run the data toolkit CLI
def main(argv: list[str] | None = None, *, tasks_file: Path | None = None) -> int:
    """Run the data toolkit CLI and return an exit code."""
    args = list(sys.argv[1:] if argv is None else argv)

    if not args or args[0] in {"-h", "--help", "help"}:
        _print_help(stream=sys.stdout if args and args[0] in {"-h", "--help", "help"} else sys.stderr)
        return 0 if args and args[0] in {"-h", "--help", "help"} else 1

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
            _print_error_with_help("Error: 'tag' requires a tag name.")
            return 1
        cmd_tag(tasks, args[1])
        return 0

    _print_error_with_help(_unknown_command_message(command))
    return 1
