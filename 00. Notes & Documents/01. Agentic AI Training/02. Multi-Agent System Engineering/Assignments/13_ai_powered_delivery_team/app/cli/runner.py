"""CLI argument parsing and command dispatch."""

from __future__ import annotations

import sys

from app.cli.commands import cmd_run
from app.config import FEATURE_REQUEST, HELP_TEXT


# _print_help - print the help text
def _print_help(*, stream: object | None = None) -> None:
    print(HELP_TEXT, file=stream if stream is not None else sys.stderr, end="")


# main - run the AI-powered delivery team CLI
def main(argv: list[str] | None = None) -> int:
    """Run the AI-powered delivery team CLI and return an exit code."""
    args = list(sys.argv[1:] if argv is None else argv)

    if args and args[0] in {"-h", "--help", "help"}:
        _print_help(stream=sys.stdout)
        return 0

    save_outputs = "--save" in args
    positional = [arg for arg in args if arg != "--save"]
    if any(arg.startswith("-") for arg in positional):
        _print_help()
        return 1

    feature_request = " ".join(positional).strip() or FEATURE_REQUEST
    return cmd_run(feature_request, save_outputs=save_outputs)
