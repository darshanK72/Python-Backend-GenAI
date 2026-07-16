"""CLI argument parsing and command dispatch."""

from __future__ import annotations

import sys

from app.cli.commands import cmd_ask, cmd_demo
from app.config import HELP_TEXT


# _print_help - print the help text
def _print_help(*, stream: object | None = None) -> None:
    print(HELP_TEXT, file=stream if stream is not None else sys.stderr, end="")


# main - run the unified engineering assistant CLI
def main(argv: list[str] | None = None) -> int:
    """Run the unified engineering assistant CLI and return an exit code."""
    args = list(sys.argv[1:] if argv is None else argv)

    if not args or args[0] in {"-h", "--help", "help"}:
        _print_help(
            stream=sys.stdout if args and args[0] in {"-h", "--help", "help"} else None
        )
        return 0 if args and args[0] in {"-h", "--help", "help"} else 1

    if args[0].lower() == "demo":
        return cmd_demo()

    question = " ".join(args).strip()
    if not question:
        _print_help()
        return 1

    return cmd_ask(question)
