"""Shared pytest fixtures."""

from __future__ import annotations

from collections.abc import Iterator
from pathlib import Path
from types import SimpleNamespace
from typing import Any
from unittest.mock import MagicMock

import pytest

from app.config import DEFAULT_REPORTS_FILE, Settings, get_settings
from app.services.token_tracker import TokenTracker

# SAMPLE_REPORT - sample bug report text for strategy tests
SAMPLE_REPORT = (
    "the app crashes when I hit save on the settings page on my iphone, "
    "super urgent, happens every time"
)

# VALID_JSON - sample valid structured extraction JSON
VALID_JSON = (
    '{"summary":"App crashes on save","component":"settings",'
    '"severity":"critical","reproducible":true}'
)


# make_chat_response - build a mocked OpenAI chat completion response
def make_chat_response(
    content: str,
    *,
    prompt_tokens: int = 10,
    completion_tokens: int = 5,
) -> Any:
    return SimpleNamespace(
        choices=[SimpleNamespace(message=SimpleNamespace(content=content))],
        usage=SimpleNamespace(
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
        ),
    )


# mock_client - return a mocked OpenAI chat client
@pytest.fixture
def mock_client() -> MagicMock:
    client = MagicMock()
    client.chat.completions.create.return_value = make_chat_response("plain text")
    return client


# token_tracker - return a fresh TokenTracker instance
@pytest.fixture
def token_tracker() -> TokenTracker:
    return TokenTracker()


# test_settings - return isolated settings for service tests
@pytest.fixture
def test_settings() -> Settings:
    return Settings.model_construct(
        openai_api_key="test-key",
        openai_model="gpt-4o-mini",
        extraction_temperature=0.0,
    )


# clear_settings_cache - clear cached settings before and after each test
@pytest.fixture(autouse=True)
def clear_settings_cache() -> Iterator[None]:
    get_settings.cache_clear()
    yield
    get_settings.cache_clear()


# default_reports_file - return the committed default reports fixture file
@pytest.fixture
def default_reports_file() -> Path:
    assert DEFAULT_REPORTS_FILE.is_file()
    return DEFAULT_REPORTS_FILE
