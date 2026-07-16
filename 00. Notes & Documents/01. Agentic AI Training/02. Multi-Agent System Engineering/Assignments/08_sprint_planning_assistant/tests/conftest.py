"""Shared pytest fixtures."""

from __future__ import annotations

from collections.abc import Iterator
from types import SimpleNamespace
from typing import Any
from unittest.mock import MagicMock

import pytest

from app.config import Settings, get_settings
from app.services.llm_service import LLMService
from app.services.mcp_client import MCPClientWrapper


# make_chat_response - build a minimal OpenAI-style chat completion response
def make_chat_response(content: str) -> Any:
    return SimpleNamespace(
        choices=[SimpleNamespace(message=SimpleNamespace(content=content))]
    )


# mock_client - provide a mocked OpenAI chat client
@pytest.fixture
def mock_client() -> MagicMock:
    client = MagicMock()
    client.chat.completions.create.return_value = make_chat_response("ok")
    return client


# test_settings - provide deterministic settings for unit tests
@pytest.fixture
def test_settings() -> Settings:
    return Settings.model_construct(
        openai_api_key="test-key",
        openai_model="gpt-4o-mini",
        llm_temperature=0.0,
    )


# llm_service - provide an LLMService wired to mocked settings and client
@pytest.fixture
def llm_service(test_settings: Settings, mock_client: MagicMock) -> LLMService:
    return LLMService(settings=test_settings, client=mock_client)


# mock_mcp - provide an in-memory MCP tool handler for tests
@pytest.fixture
def mock_mcp() -> MCPClientWrapper:
    backlog_state = {
        "tasks": [
            {"title": "DB migration", "assignee": "", "story_points": 8, "status": "todo", "risk_level": "high"},
            {"title": "Auth token refresh", "assignee": "Sam", "story_points": 5, "status": "in_progress", "risk_level": "medium"},
        ]
    }

    def handler(name: str, arguments: dict[str, Any]) -> str:
        if name == "get_backlog":
            lines = []
            for index, task in enumerate(backlog_state["tasks"], start=1):
                lines.append(
                    f"{index}. {task['title']} — {task['story_points']} SP, "
                    f"status={task['status']}, assignee={task['assignee'] or 'unassigned'}, "
                    f"risk={task['risk_level']}"
                )
            return "\n".join(lines)
        if name == "add_task":
            backlog_state["tasks"].append(
                {
                    "title": arguments["title"],
                    "assignee": arguments["assignee"],
                    "story_points": arguments["story_points"],
                    "status": "todo",
                    "risk_level": "low",
                }
            )
            return (
                f"Task added: {arguments['title']} "
                f"({arguments['story_points']} SP, assigned to {arguments['assignee']})"
            )
        if name == "check_capacity":
            total = sum(
                task["story_points"]
                for task in backlog_state["tasks"]
                if task["status"] != "done"
            )
            velocity = int(arguments.get("velocity", 40))
            if total > velocity:
                return f"Sprint is at {total}/{velocity} SP. Over capacity by {total - velocity} SP."
            return f"Sprint is at {total}/{velocity} SP. Under capacity by {velocity - total} SP."
        if name == "get_risk_summary":
            risky = [
                task for task in backlog_state["tasks"] if task["risk_level"] in {"high", "medium"}
            ]
            lines = []
            for index, task in enumerate(risky, start=1):
                lines.append(
                    f"{index}. {task['title']} — {task['story_points']} SP, "
                    f"status={task['status']}, risk={task['risk_level']}"
                )
            return "\n".join(lines)
        raise ValueError(f"Unknown tool {name}")

    return MCPClientWrapper(tool_handler=handler)


# clear_settings_cache - reset the cached settings singleton between tests
@pytest.fixture(autouse=True)
def clear_settings_cache() -> Iterator[None]:
    get_settings.cache_clear()
    yield
    get_settings.cache_clear()
