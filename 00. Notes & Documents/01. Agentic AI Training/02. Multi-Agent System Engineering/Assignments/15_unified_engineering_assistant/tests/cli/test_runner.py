"""Tests for the CLI runner."""

from __future__ import annotations

from unittest.mock import patch

from app.cli.runner import main


# test_main_without_args - test that missing args prints usage and exits 1
def test_main_without_args(capsys) -> None:
    assert main([]) == 1
    assert "Usage:" in capsys.readouterr().err


# test_main_help_prints_usage - test that --help prints usage to stdout and exits 0
def test_main_help_prints_usage(capsys) -> None:
    assert main(["--help"]) == 0
    captured = capsys.readouterr()
    assert "Usage:" in captured.out
    assert "mcp_server.py" in captured.out
    assert captured.err == ""


# test_main_demo - test that demo mode runs the four-query session
def test_main_demo() -> None:
    with patch("app.cli.runner.cmd_demo", return_value=0) as demo_mock:
        assert main(["demo"]) == 0
    demo_mock.assert_called_once()


# test_main_single_question - test that a question argument runs cmd_ask
def test_main_single_question() -> None:
    with patch("app.cli.runner.cmd_ask", return_value=0) as ask_mock:
        assert main(["Which", "tasks", "are", "blocked?"]) == 0
    ask_mock.assert_called_once_with("Which tasks are blocked?")


# test_main_reports_mcp_server_down - test that unreachable MCP errors are surfaced
def test_main_reports_mcp_server_down(capsys) -> None:
    with patch(
        "app.cli.commands.run_query",
        side_effect=RuntimeError(
            "MCP server is not reachable at http://127.0.0.1:8000/mcp.\n"
            "Start it in a separate terminal first:\n"
            "  python mcp_server.py"
        ),
    ):
        assert main(["What is microservices?"]) == 1
    assert "mcp_server.py" in capsys.readouterr().err


# test_main_reports_missing_api_key - test that missing API key errors are surfaced
def test_main_reports_missing_api_key(capsys) -> None:
    with patch(
        "app.cli.commands.run_query",
        side_effect=RuntimeError("OPENAI_API_KEY is not set in the environment."),
    ):
        assert main(["What is DevOps?"]) == 1
    assert "OPENAI_API_KEY" in capsys.readouterr().err
