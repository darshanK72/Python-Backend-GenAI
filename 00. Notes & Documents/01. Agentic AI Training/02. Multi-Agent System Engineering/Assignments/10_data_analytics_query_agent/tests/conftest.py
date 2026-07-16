"""Shared pytest fixtures."""

from __future__ import annotations

from collections.abc import Iterator
from pathlib import Path
from types import SimpleNamespace
from typing import Any
from unittest.mock import MagicMock

import pytest

from app.config import Settings, get_settings
from app.services.database import get_connection, load_schema_map
from app.services.llm_service import LLMService
from seed_db import create_database


# make_chat_response - build a minimal OpenAI-style chat completion response
def make_chat_response(content: str) -> Any:
    return SimpleNamespace(
        choices=[SimpleNamespace(message=SimpleNamespace(content=content))]
    )


# mock_client - provide a mocked OpenAI chat client
@pytest.fixture
def mock_client() -> MagicMock:
    client = MagicMock()
    client.chat.completions.create.return_value = make_chat_response("SELECT 1")
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


# temp_db - create a temporary seeded analytics database
@pytest.fixture
def temp_db(tmp_path: Path) -> Path:
    db_path = tmp_path / "analytics.db"
    create_database(db_path)
    return db_path


# db_conn - open a connection to the temporary seeded database
@pytest.fixture
def db_conn(temp_db: Path):
    conn = get_connection(temp_db)
    yield conn
    conn.close()


# schema_map - load table→column map from the temporary database
@pytest.fixture
def schema_map(db_conn) -> dict[str, list[str]]:
    return load_schema_map(db_conn)


# clear_settings_cache - reset the cached settings singleton between tests
@pytest.fixture(autouse=True)
def clear_settings_cache() -> Iterator[None]:
    get_settings.cache_clear()
    yield
    get_settings.cache_clear()
