"""Tests for prompting strategy entry points."""

from __future__ import annotations

import pytest

from app.schemas.extraction import FEWSHOT_EXAMPLES, SYSTEM_PROMPT
from app.services.json_parser import StructuredParseError
from app.services.llm_service import LLMService
from app.strategies.extraction import (
    build_fewshot_messages,
    build_naive_messages,
    build_structured_messages,
    fewshot_extract,
    naive_extract,
    structured_extract,
)
from tests.conftest import SAMPLE_REPORT, VALID_JSON, make_chat_response


def test_build_naive_messages_contains_report() -> None:
    messages = build_naive_messages(SAMPLE_REPORT)

    assert len(messages) == 1
    assert messages[0]["role"] == "user"
    assert SAMPLE_REPORT in messages[0]["content"]


def test_build_structured_messages_uses_system_prompt() -> None:
    messages = build_structured_messages(SAMPLE_REPORT)

    assert messages[0]["content"] == SYSTEM_PROMPT
    assert SAMPLE_REPORT in messages[1]["content"]


def test_build_fewshot_messages_includes_examples() -> None:
    messages = build_fewshot_messages(SAMPLE_REPORT)

    assert messages[0]["content"] == SYSTEM_PROMPT
    assert len(messages) == 1 + len(FEWSHOT_EXAMPLES) + 1
    assert SAMPLE_REPORT in messages[-1]["content"]


def test_naive_extract_returns_raw_text(mock_client, test_settings, token_tracker) -> None:
    service = LLMService(settings=test_settings, token_tracker=token_tracker, client=mock_client)

    result = naive_extract(SAMPLE_REPORT, service=service)

    assert result == "plain text"


def test_structured_extract_returns_dict(mock_client, test_settings, token_tracker) -> None:
    mock_client.chat.completions.create.return_value = make_chat_response(VALID_JSON)
    service = LLMService(settings=test_settings, token_tracker=token_tracker, client=mock_client)

    result = structured_extract(SAMPLE_REPORT, service=service)

    assert result["severity"] == "critical"
    assert result["reproducible"] is True


def test_fewshot_extract_returns_dict(mock_client, test_settings, token_tracker) -> None:
    mock_client.chat.completions.create.return_value = make_chat_response(VALID_JSON)
    service = LLMService(settings=test_settings, token_tracker=token_tracker, client=mock_client)

    result = fewshot_extract(SAMPLE_REPORT, service=service)

    assert result["component"] == "settings"


def test_structured_extract_surfaces_parse_failure(mock_client, test_settings, token_tracker) -> None:
    mock_client.chat.completions.create.side_effect = [
        make_chat_response("bad"),
        make_chat_response("still bad"),
    ]
    service = LLMService(settings=test_settings, token_tracker=token_tracker, client=mock_client)

    with pytest.raises(StructuredParseError):
        structured_extract(SAMPLE_REPORT, service=service)
