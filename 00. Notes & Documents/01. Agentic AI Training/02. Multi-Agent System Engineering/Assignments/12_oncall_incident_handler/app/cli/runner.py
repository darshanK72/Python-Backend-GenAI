"""CLI argument parsing and command dispatch."""

from __future__ import annotations

import sys

from app.cli.commands import cmd_demo, cmd_incident, resolve_incident_path
from app.config import HELP_TEXT


# _print_help - print the help text
def _print_help(*, stream: object = sys.stderr) -> None:
    print(HELP_TEXT, file=stream, end="")


# main - run the on-call incident handler CLI
def main(argv: list[str] | None = None) -> int:
    """Run the on-call incident handler CLI and return an exit code."""
    args = list(sys.argv[1:] if argv is None else argv)

    if not args or args[0] in {"-h", "--help", "help"}:
        _print_help(
            stream=sys.stdout if args and args[0] in {"-h", "--help", "help"} else sys.stderr
        )
        return 0 if args and args[0] in {"-h", "--help", "help"} else 1

    if args[0].lower() == "demo":
        return cmd_demo()

    return cmd_incident(resolve_incident_path(args[0]))
