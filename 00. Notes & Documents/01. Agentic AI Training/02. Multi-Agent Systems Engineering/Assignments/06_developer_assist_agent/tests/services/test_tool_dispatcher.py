"""Tests for tool dispatching."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from app.services.tool_dispatcher import ToolDispatchError, dispatch_tool


def test_dispatch_story_estimator(llm_service, mock_client: MagicMock) -> None:
    mock_client.chat.completions.create.return_value = MagicMock(
        choices=[
            MagicMock(
                message=MagicMock(
                    content="5 points — export is straightforward. No new infrastructure needed."
                )
            )
        ]
    )
    result = dispatch_tool(
        "story_estimator",
        "CSV export feature",
        service=llm_service,
    )
    assert "5 points" in result


def test_dispatch_unknown_action_raises() -> None:
    with pytest.raises(ToolDispatchError):
        dispatch_tool("missing_tool", "input")
