"""Tests for the CLI runner."""

from __future__ import annotations

from unittest.mock import patch

from app.cli.runner import main
from app.graph.state import initial_state


# test_main_without_args_prints_usage - test that missing args prints usage and exits 1
def test_main_without_args_prints_usage(capsys) -> None:
    assert main([]) == 1
    captured = capsys.readouterr()
    assert "Usage:" in captured.err


# test_main_help_prints_usage - test that --help prints usage to stdout and exits 0
def test_main_help_prints_usage(capsys) -> None:
    assert main(["--help"]) == 0
    captured = capsys.readouterr()
    assert "Usage:" in captured.out
    assert captured.err == ""


# test_main_unknown_command_treated_as_question - test that a free-text arg runs ask mode
def test_main_unknown_command_treated_as_question(capsys) -> None:
    final_state = initial_state("hello")
    final_state["final_answer"] = "ok"
    final_state["stopped_reason"] = "final_answer"

    with patch("app.cli.commands.run_agent", return_value=final_state):
        assert main(["hello"]) == 0


# test_main_demo_runs_four_queries - test that demo mode runs all four sample queries
def test_main_demo_runs_four_queries(capsys) -> None:
    final_state = initial_state("demo")
    final_state["final_answer"] = "ok"
    final_state["stopped_reason"] = "final_answer"

    with patch("app.cli.commands.run_agent", return_value=final_state) as run_mock:
        assert main(["demo"]) == 0
    assert run_mock.call_count == 4


# test_main_reports_missing_api_key - test that missing API key errors are surfaced
def test_main_reports_missing_api_key(capsys) -> None:
    with patch(
        "app.cli.commands.run_agent",
        side_effect=RuntimeError("OPENAI_API_KEY is not set"),
    ):
        assert main(["Estimate CSV export"]) == 1
    captured = capsys.readouterr()
    assert "OPENAI_API_KEY" in captured.err
