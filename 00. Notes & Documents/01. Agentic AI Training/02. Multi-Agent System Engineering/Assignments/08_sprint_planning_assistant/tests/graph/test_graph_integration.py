"""Integration tests for the supervisor graph."""

from __future__ import annotations

from unittest.mock import MagicMock

from app.cli.commands import DEMO_REQUESTS
from app.graph.builder import build_graph
from app.graph.state import initial_state
from app.services.llm_service import LLMService

# PLAN_JSON - sample sprint builder task plan JSON
PLAN_JSON = """{
  "feature": "OAuth login",
  "tasks": [
    {"title": "Add OAuth callback route", "assignee": "Sam", "story_points": 3},
    {"title": "Store provider tokens", "assignee": "Alex", "story_points": 5},
    {"title": "Add login button", "assignee": "Sam", "story_points": 2}
  ]
}"""

# RISK_TEXT - sample risk assessor output
RISK_TEXT = """1. DB migration — no assignee and 8 SP blocks other work.
2. Auth token refresh — in progress but depends on external key rotation."""


# test_demo_session_uses_all_workers - test demo session routes through all three workers
def test_demo_session_uses_all_workers(test_settings, mock_mcp, mock_client) -> None:
    mock_client.chat.completions.create.side_effect = [
        _response(PLAN_JSON),
        _response(RISK_TEXT),
        _response(PLAN_JSON),
    ]
    llm = LLMService(settings=test_settings, client=mock_client)
    result = build_graph(llm, mock_mcp).invoke(initial_state(DEMO_REQUESTS))

    assert len(result["results"]) == 4
    assert any("Created 3 tasks" in item for item in result["results"])
    assert any("Sprint is at" in item for item in result["results"])
    assert "DB migration" in result["results"][2]
    assert len(mock_mcp.call_log) >= 5
    assert result["finished"] is True


# _response - build a mocked chat completion response
def _response(content: str) -> MagicMock:
    return MagicMock(
        choices=[MagicMock(message=MagicMock(content=content))]
    )
