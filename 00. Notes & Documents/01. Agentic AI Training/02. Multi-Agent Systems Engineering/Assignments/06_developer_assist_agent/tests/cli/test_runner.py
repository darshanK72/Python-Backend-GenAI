"""Tests for the CLI runner."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

from app.cli.runner import main
from app.graph.state import initial_state


def test_main_without_args_prints_usage(capsys) -> None:
    assert main([]) == 1
    captured = capsys.readouterr()
    assert "Usage:" in captured.err


def test_main_unknown_command_treated_as_question(capsys) -> None:
    final_state = initial_state("hello")
    final_state["final_answer"] = "ok"
    final_state["stopped_reason"] = "final_answer"

    with patch("app.cli.runner.run_agent", return_value=final_state):
        assert main(["hello"]) == 0


def test_main_demo_runs_four_queries(capsys) -> None:
    final_state = initial_state("demo")
    final_state["final_answer"] = "ok"
    final_state["stopped_reason"] = "final_answer"

    with patch("app.cli.runner.run_agent", return_value=final_state) as run_mock:
        assert main(["demo"]) == 0
    assert run_mock.call_count == 4


def test_main_reports_missing_api_key(capsys) -> None:
    with patch("app.cli.runner.run_agent", side_effect=RuntimeError("OPENAI_API_KEY is not set")):
        assert main(["Estimate CSV export"]) == 1
    captured = capsys.readouterr()
    assert "OPENAI_API_KEY" in captured.err
