"""CLI argument parsing and command dispatch for the WriterAgent."""

from __future__ import annotations

import sys

from app.cli.commands import cmd_demo, cmd_topic
from app.config import HELP_TEXT


# _print_help - print the help text
def _print_help(*, stream: object | None = None) -> None:
    print(HELP_TEXT, file=stream if stream is not None else sys.stderr, end="")


# main - run the WriterAgent CLI
def main(argv: list[str] | None = None) -> int:
    """Run the WriterAgent CLI and return an exit code."""
    args = list(sys.argv[1:] if argv is None else argv)

    if not args:
        _print_help()
        return 1

    if args[0] in {"-h", "--help", "help"}:
        _print_help(stream=sys.stdout)
        return 0

    if args[0].lower() == "demo":
        return cmd_demo()

    topic = " ".join(args).strip()
    if not topic:
        _print_help()
        return 1

    return cmd_topic(topic)
