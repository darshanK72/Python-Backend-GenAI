"""Tests for the CLI runner."""

from __future__ import annotations

from unittest.mock import patch

from app.cli.runner import main
from app.graph.state import initial_state


# test_main_without_args - test that missing args prints usage and exits 1
def test_main_without_args(capsys) -> None:
    assert main([]) == 1
    assert "Usage:" in capsys.readouterr().err


# test_main_help_prints_usage - test that --help prints usage to stdout and exits 0
def test_main_help_prints_usage(capsys) -> None:
    assert main(["--help"]) == 0
    captured = capsys.readouterr()
    assert "Usage:" in captured.out
    assert captured.err == ""


# test_main_demo - test that demo mode runs the full evaluator session
def test_main_demo(capsys) -> None:
    state = initial_state(["Done"])
    state["finished"] = True
    with patch("app.cli.commands.run_session", return_value=state):
        assert main(["demo"]) == 0


# test_main_single_request - test that a request argument runs the session
def test_main_single_request(capsys) -> None:
    state = initial_state(["Check capacity"])
    state["finished"] = True
    with patch("app.cli.commands.run_session", return_value=state):
        assert main(["Check capacity"]) == 0


# test_main_reports_missing_api_key - test that missing API key errors are surfaced
def test_main_reports_missing_api_key(capsys) -> None:
    with patch(
        "app.cli.commands.run_session",
        side_effect=RuntimeError("OPENAI_API_KEY is not set"),
    ):
        assert main(["Check capacity"]) == 1
    captured = capsys.readouterr()
    assert "OPENAI_API_KEY" in captured.err
