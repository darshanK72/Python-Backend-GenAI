"""Tests for the CLI runner."""

from __future__ import annotations

from unittest.mock import patch

from app.cli.runner import main
from app.config import FEATURE_REQUEST

# SAMPLE_REPORT - minimal valid five-section delivery report for CLI mocks
SAMPLE_REPORT = "\n".join(
    [
        "## Executive Summary",
        "## Technical Design",
        "## Test Coverage",
        "## Deployment Configuration",
        "## Open Questions",
    ]
)


# test_main_help_prints_usage - test that --help prints usage to stdout and exits 0
def test_main_help_prints_usage(capsys) -> None:
    assert main(["--help"]) == 0
    captured = capsys.readouterr()
    assert "Usage:" in captured.out
    assert captured.err == ""


# test_main_runs_delivery_by_default - test that default mode uses FEATURE_REQUEST
def test_main_runs_delivery_by_default(capsys) -> None:
    with patch("app.cli.commands.run_delivery", return_value=("transcript", SAMPLE_REPORT)) as run_mock:
        assert main([]) == 0
    run_mock.assert_called_once_with(FEATURE_REQUEST, save_outputs=False)


# test_main_save_flag - test that --save passes save_outputs=True
def test_main_save_flag(capsys) -> None:
    with patch("app.cli.commands.run_delivery", return_value=("chat", SAMPLE_REPORT)) as run_mock:
        assert main(["--save"]) == 0
    run_mock.assert_called_once_with(FEATURE_REQUEST, save_outputs=True)


# test_main_custom_feature_request - test that free-text args override FEATURE_REQUEST
def test_main_custom_feature_request(capsys) -> None:
    custom = "Add OAuth login for GitHub accounts"
    with patch("app.cli.commands.run_delivery", return_value=("chat", SAMPLE_REPORT)) as run_mock:
        assert main([custom]) == 0
    run_mock.assert_called_once_with(custom, save_outputs=False)


# test_main_custom_feature_with_save - test custom feature plus --save
def test_main_custom_feature_with_save(capsys) -> None:
    custom = "Add CSV export for the backlog"
    with patch("app.cli.commands.run_delivery", return_value=("chat", SAMPLE_REPORT)) as run_mock:
        assert main(["--save", custom]) == 0
    run_mock.assert_called_once_with(custom, save_outputs=True)


# test_main_rejects_unknown_flags - test that unknown flags print usage and exit 1
def test_main_rejects_unknown_flags(capsys) -> None:
    assert main(["--bogus"]) == 1
    assert "Usage:" in capsys.readouterr().err


# test_main_reports_missing_api_key - test that missing API key errors are surfaced
def test_main_reports_missing_api_key(capsys) -> None:
    with patch(
        "app.cli.commands.run_delivery",
        side_effect=RuntimeError("OPENAI_API_KEY is not set in the environment."),
    ):
        assert main([]) == 1
    assert "OPENAI_API_KEY" in capsys.readouterr().err
