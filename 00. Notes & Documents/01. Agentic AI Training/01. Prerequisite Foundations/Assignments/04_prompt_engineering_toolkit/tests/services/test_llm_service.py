"""Tests for the OpenAI chat wrapper."""

from __future__ import annotations

import pytest

from app.schemas.extraction import CORRECTIVE_JSON_INSTRUCTION
from app.services.json_parser import StructuredParseError
from app.services.llm_service import LLMService
from tests.conftest import VALID_JSON, make_chat_response


# test_chat_records_tokens - test that chat records token usage and returns assistant text
def test_chat_records_tokens(mock_client, test_settings, token_tracker) -> None:
    service = LLMService(
        settings=test_settings,
        token_tracker=token_tracker,
        client=mock_client,
    )

    content = service.chat([{"role": "user", "content": "hello"}])

    assert content == "plain text"
    assert token_tracker.running_total == 15
    mock_client.chat.completions.create.assert_called_once_with(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "hello"}],
        temperature=0.0,
    )


# test_chat_without_api_key_raises - test that chat raises when OPENAI_API_KEY is missing
def test_chat_without_api_key_raises(test_settings, token_tracker) -> None:
    test_settings.openai_api_key = ""
    service = LLMService(settings=test_settings, token_tracker=token_tracker)

    with pytest.raises(RuntimeError, match="OPENAI_API_KEY"):
        service.chat([{"role": "user", "content": "hello"}])


# test_parse_structured_parses_valid_json - test that parse_structured parses valid JSON without retry
def test_parse_structured_parses_valid_json(mock_client, test_settings, token_tracker) -> None:
    mock_client.chat.completions.create.return_value = make_chat_response(VALID_JSON)
    service = LLMService(settings=test_settings, token_tracker=token_tracker, client=mock_client)

    result = service.parse_structured(
        VALID_JSON,
        [{"role": "user", "content": "bug"}],
        corrective_instruction=CORRECTIVE_JSON_INSTRUCTION,
    )

    assert result["severity"] == "critical"
    mock_client.chat.completions.create.assert_not_called()


# test_parse_structured_retries_on_invalid_json - test that parse_structured retries once on invalid JSON
def test_parse_structured_retries_on_invalid_json(mock_client, test_settings, token_tracker) -> None:
    mock_client.chat.completions.create.return_value = make_chat_response(VALID_JSON)
    service = LLMService(settings=test_settings, token_tracker=token_tracker, client=mock_client)
    messages = [{"role": "user", "content": "bug"}]

    result = service.parse_structured(
        "not json",
        messages,
        corrective_instruction=CORRECTIVE_JSON_INSTRUCTION,
    )

    assert result["component"] == "settings"
    mock_client.chat.completions.create.assert_called_once()


# test_parse_structured_raises_after_failed_retry - test that parse_structured raises after a failed retry
def test_parse_structured_raises_after_failed_retry(mock_client, test_settings, token_tracker) -> None:
    mock_client.chat.completions.create.side_effect = [
        make_chat_response("still not json"),
        make_chat_response("also not json"),
    ]
    service = LLMService(settings=test_settings, token_tracker=token_tracker, client=mock_client)

    with pytest.raises(StructuredParseError, match="after retry"):
        service.parse_structured(
            "still not json",
            [{"role": "user", "content": "bug"}],
            corrective_instruction=CORRECTIVE_JSON_INSTRUCTION,
        )
