"""Tests for the CLI runner."""

from __future__ import annotations

from unittest.mock import patch

from app.cli.runner import main
from app.config import DATA_DIR, INCIDENT_FILES


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


# test_main_demo - test that demo mode runs all three sample incidents
def test_main_demo(capsys) -> None:
    with patch("app.cli.commands.run_incident", return_value={}) as run_mock:
        assert main(["demo"]) == 0
    assert run_mock.call_count == 3
    assert [call.args[0] for call in run_mock.call_args_list] == INCIDENT_FILES


# test_main_single_incident - test that a path runs ask mode via run_incident
def test_main_single_incident(capsys) -> None:
    path = DATA_DIR / "incident_01.json"
    with patch("app.cli.commands.run_incident", return_value={}) as run_mock:
        assert main([str(path)]) == 0
    run_mock.assert_called_once()
    assert run_mock.call_args.args[0] == path


# test_main_resolves_basename_under_data - test that bare filenames resolve under data/
def test_main_resolves_basename_under_data(capsys) -> None:
    with patch("app.cli.commands.run_incident", return_value={}) as run_mock:
        assert main(["incident_01.json"]) == 0
    assert run_mock.call_args.args[0] == DATA_DIR / "incident_01.json"


# test_main_reports_missing_file - test that missing incident files exit 1
def test_main_reports_missing_file(capsys) -> None:
    assert main(["missing_incident.json"]) == 1
    assert "not found" in capsys.readouterr().err


# test_main_reports_missing_api_key - test that missing API key errors are surfaced
def test_main_reports_missing_api_key(capsys) -> None:
    with patch(
        "app.cli.commands.run_incident",
        side_effect=RuntimeError("OPENAI_API_KEY is not set in the environment."),
    ):
        assert main([str(DATA_DIR / "incident_01.json")]) == 1
    assert "OPENAI_API_KEY" in capsys.readouterr().err
