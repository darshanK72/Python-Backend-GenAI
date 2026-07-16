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


# test_main_demo_runs_two_topics - test that demo mode runs both evaluator topics
def test_main_demo_runs_two_topics(capsys) -> None:
    state = initial_state("topic")
    state["article"] = "done"
    with patch("app.cli.commands.run_brief", return_value=state) as run_mock:
        assert main(["demo"]) == 0
    assert run_mock.call_count == 2


# test_main_single_topic - test that a topic argument runs the brief pipeline
def test_main_single_topic(capsys) -> None:
    state = initial_state("Event-driven architecture")
    state["article"] = "brief"
    with patch("app.cli.commands.run_brief", return_value=state):
        assert main(["Event-driven architecture"]) == 0


# test_main_reports_missing_api_key - test that missing API key errors are surfaced
def test_main_reports_missing_api_key(capsys) -> None:
    with patch(
        "app.cli.commands.run_brief",
        side_effect=RuntimeError("OPENAI_API_KEY is not set"),
    ):
        assert main(["Event-driven architecture"]) == 1
    captured = capsys.readouterr()
    assert "OPENAI_API_KEY" in captured.err
