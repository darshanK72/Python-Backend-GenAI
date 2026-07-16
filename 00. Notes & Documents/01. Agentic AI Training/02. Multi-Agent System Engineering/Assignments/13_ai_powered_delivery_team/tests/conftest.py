"""Shared pytest fixtures."""

from __future__ import annotations

from collections.abc import Iterator

import pytest

from app.config import Settings, get_settings


# test_settings - Settings constructed without reading the real environment
@pytest.fixture
def test_settings() -> Settings:
    return Settings.model_construct(
        openai_api_key="test-key",
        openai_model="gpt-4o-mini",
        llm_temperature=0.0,
    )


# clear_settings_cache - clear get_settings LRU cache around each test
@pytest.fixture(autouse=True)
def clear_settings_cache() -> Iterator[None]:
    get_settings.cache_clear()
    yield
    get_settings.cache_clear()
