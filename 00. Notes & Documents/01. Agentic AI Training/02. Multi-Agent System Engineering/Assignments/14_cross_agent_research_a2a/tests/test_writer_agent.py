"""Tests for the WriterAgent CLI."""

from __future__ import annotations

from unittest.mock import patch

from app.cli.runner import main
from app.config import DEMO_TOPICS


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


# test_main_demo - test that demo mode runs both evaluator topics
def test_main_demo() -> None:
    result = {
        "topic": "x",
        "task_id": "t",
        "research_result": "r",
        "article": "article",
        "agent_card": {},
    }
    with patch("app.cli.commands.run_brief", return_value=result) as brief_mock:
        assert main(["demo"]) == 0
    assert brief_mock.call_count == len(DEMO_TOPICS)


# test_main_single_topic - test that a free-text topic runs cmd_topic
def test_main_single_topic() -> None:
    result = {
        "topic": "Event-driven architecture",
        "task_id": "t",
        "research_result": "r",
        "article": "article",
        "agent_card": {},
    }
    with patch("app.cli.commands.run_brief", return_value=result) as brief_mock:
        assert main(["Event-driven architecture"]) == 0
    brief_mock.assert_called_once()
    assert brief_mock.call_args.args[0] == "Event-driven architecture"


# test_main_reports_research_agent_down - test unreachable ResearchAgent errors are surfaced
def test_main_reports_research_agent_down(capsys) -> None:
    with patch(
        "app.cli.commands.run_brief",
        side_effect=RuntimeError(
            "ResearchAgent unreachable at http://localhost:8001. "
            "Start it first with: uvicorn research_agent:app --port 8001"
        ),
    ):
        assert main(["Event-driven architecture"]) == 1
    assert "ResearchAgent unreachable" in capsys.readouterr().err
