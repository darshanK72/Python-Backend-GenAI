"""Tests for LLM service."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from fastapi import HTTPException

from app.schemas.llm import ClassifyResult, SummariseResult
from app.services.llm_service import LLMService
from tests.conftest import make_chat_response

VALID_SUMMARY_JSON = '{"summary":"Short summary.","word_count":2}'
VALID_CLASSIFY_JSON = (
    '{"category":"feature","confidence":0.8,'
    '"rationale":"User requests a new capability."}'
)


def test_summarise_text_returns_validated_model(
    llm_service: LLMService,
    mock_client: MagicMock,
) -> None:
    mock_client.chat.completions.create.return_value = make_chat_response(VALID_SUMMARY_JSON)

    result = llm_service.summarise_text("Long text here.")

    assert isinstance(result, SummariseResult)
    assert result.word_count == 2


def test_classify_text_returns_validated_model(
    llm_service: LLMService,
    mock_client: MagicMock,
) -> None:
    mock_client.chat.completions.create.return_value = make_chat_response(VALID_CLASSIFY_JSON)

    result = llm_service.classify_text("Can we add dark mode?")

    assert isinstance(result, ClassifyResult)
    assert result.category == "feature"


def test_summarise_retries_on_invalid_json(
    llm_service: LLMService,
    mock_client: MagicMock,
) -> None:
    mock_client.chat.completions.create.side_effect = [
        make_chat_response("bad"),
        make_chat_response(VALID_SUMMARY_JSON),
    ]

    result = llm_service.summarise_text("Some text.")

    assert result.summary == "Short summary."
    assert mock_client.chat.completions.create.call_count == 2


def test_missing_openai_key_raises_502(test_settings) -> None:
    test_settings.openai_api_key = ""
    service = LLMService(settings=test_settings)

    with pytest.raises(HTTPException) as exc_info:
        service.summarise_text("text")

    assert exc_info.value.status_code == 502


def test_invalid_json_after_retry_raises_502(
    llm_service: LLMService,
    mock_client: MagicMock,
) -> None:
    mock_client.chat.completions.create.side_effect = [
        make_chat_response("bad"),
        make_chat_response("still bad"),
    ]

    with pytest.raises(HTTPException) as exc_info:
        llm_service.classify_text("text")

    assert exc_info.value.status_code == 502
