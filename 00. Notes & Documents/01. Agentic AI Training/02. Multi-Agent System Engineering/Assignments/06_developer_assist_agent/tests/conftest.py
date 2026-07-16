"""Shared pytest fixtures."""

from __future__ import annotations

from collections.abc import Iterator
from types import SimpleNamespace
from typing import Any
from unittest.mock import MagicMock

import pytest

from app.config import Settings, get_settings
from app.services.llm_service import LLMService


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


# clear_settings_cache - reset the cached settings singleton between tests
@pytest.fixture(autouse=True)
def clear_settings_cache() -> Iterator[None]:
    get_settings.cache_clear()
    yield
    get_settings.cache_clear()
