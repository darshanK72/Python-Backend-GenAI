"""Tests for the CLI runner."""

from __future__ import annotations

from unittest.mock import patch

from app.cli.commands import FEATURE_A, FEATURE_B
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


# test_main_demo - test that demo mode runs both evaluator features
def test_main_demo(capsys) -> None:
    state = initial_state("test")
    with patch("app.cli.commands.run_scope", return_value=state) as run_mock:
        assert main(["demo"]) == 0
    assert run_mock.call_count == 2
    run_mock.assert_any_call(FEATURE_A, service=None)
    run_mock.assert_any_call(FEATURE_B, service=None)


# test_main_single_request - test that a free-text feature request runs scope mode
def test_main_single_request(capsys) -> None:
    state = initial_state(FEATURE_A)
    with patch("app.cli.commands.run_scope", return_value=state) as run_mock:
        assert main([FEATURE_A]) == 0
    run_mock.assert_called_once_with(FEATURE_A, service=None)


# test_main_reports_missing_api_key - test that missing API key errors are surfaced
def test_main_reports_missing_api_key(capsys) -> None:
    with patch(
        "app.cli.commands.run_scope",
        side_effect=RuntimeError("OPENAI_API_KEY is not set in the environment."),
    ):
        assert main([FEATURE_A]) == 1
    captured = capsys.readouterr()
    assert "OPENAI_API_KEY" in captured.err
