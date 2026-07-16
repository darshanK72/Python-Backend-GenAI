"""CLI argument parsing and command dispatch."""

from __future__ import annotations

import sys
from pathlib import Path

from app.cli.commands import cmd_run_reports
from app.config import DEFAULT_REPORTS_FILE, HELP_TEXT
from app.services.llm_service import LLMService


# _print_help - print the help text
def _print_help(*, stream: object = sys.stderr) -> None:
    print(HELP_TEXT, file=stream, end="")


# main - run the prompt engineering toolkit CLI
def main(
    argv: list[str] | None = None,
    *,
    reports_file: Path | None = None,
    service: LLMService | None = None,
) -> int:
    """Run the prompt engineering toolkit CLI and return an exit code."""
    args = list(sys.argv[1:] if argv is None else argv)

    if args and args[0] in {"-h", "--help", "help"}:
        _print_help(stream=sys.stdout)
        return 0

    path = Path(args[0]) if args else (reports_file or DEFAULT_REPORTS_FILE)
    return cmd_run_reports(path, service=service)
