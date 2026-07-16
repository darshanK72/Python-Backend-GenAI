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


# test_main_demo - test that demo mode runs all four evaluator queries
def test_main_demo(capsys) -> None:
    state = initial_state("test", "schema")
    state["answer"] = "done"
    with patch("app.cli.commands.run_query", return_value=state) as run_mock:
        assert main(["demo"]) == 0
    assert run_mock.call_count == 4


# test_main_single_question - test that a free-text question runs ask mode
def test_main_single_question(capsys) -> None:
    state = initial_state("How many tasks are currently blocked?", "schema")
    state["answer"] = "done"
    with patch("app.cli.commands.run_query", return_value=state):
        assert main(["How many tasks are currently blocked?"]) == 0


# test_main_reports_missing_database - test that missing database errors are surfaced
def test_main_reports_missing_database(capsys) -> None:
    with patch(
        "app.cli.commands.run_query",
        side_effect=FileNotFoundError("Database not found. Run: python seed_db.py"),
    ):
        assert main(["How many tasks are currently blocked?"]) == 1
    captured = capsys.readouterr()
    assert "seed_db.py" in captured.err
