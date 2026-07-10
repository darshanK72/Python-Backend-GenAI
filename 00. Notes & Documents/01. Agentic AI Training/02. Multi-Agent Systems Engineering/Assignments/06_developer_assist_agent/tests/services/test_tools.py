"""Tests for specialist tools."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from app.services.tools import doc_summariser, story_estimator, tech_stack_advisor


def test_story_estimator_returns_points(llm_service, mock_client: MagicMock) -> None:
    mock_client.chat.completions.create.return_value = MagicMock(
        choices=[
            MagicMock(
                message=MagicMock(
                    content="3 points — small UI change. No backend work required."
                )
            )
        ]
    )
    result = story_estimator("Add a button", service=llm_service)
    assert "3 points" in result


def test_tech_stack_advisor_returns_recommendations(
    llm_service,
    mock_client: MagicMock,
) -> None:
    mock_client.chat.completions.create.return_value = MagicMock(
        choices=[
            MagicMock(
                message=MagicMock(
                    content=(
                        "FastAPI — async-native Python web framework.\n"
                        "Redis — in-memory pub/sub for real-time events."
                    )
                )
            )
        ]
    )
    result = tech_stack_advisor("real-time notifications", service=llm_service)
    assert "FastAPI" in result
    assert "Redis" in result


def test_doc_summariser_returns_three_bullets(
    llm_service,
    mock_client: MagicMock,
) -> None:
    mock_client.chat.completions.create.return_value = MagicMock(
        choices=[
            MagicMock(
                message=MagicMock(
                    content=(
                        "- LangGraph models workflows as graphs.\n"
                        "- Nodes mutate shared state.\n"
                        "- Conditional edges route control flow."
                    )
                )
            )
        ]
    )
    result = doc_summariser("LangGraph docs", service=llm_service)
    assert result.count("-") == 3


def test_story_estimator_rejects_invalid_output(
    llm_service,
    mock_client: MagicMock,
) -> None:
    mock_client.chat.completions.create.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content="Looks medium sized."))]
    )
    with pytest.raises(ValueError):
        story_estimator("feature", service=llm_service)
