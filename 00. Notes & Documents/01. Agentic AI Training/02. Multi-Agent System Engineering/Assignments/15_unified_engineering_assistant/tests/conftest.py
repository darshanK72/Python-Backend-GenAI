"""Shared pytest fixtures."""

from __future__ import annotations

from collections.abc import Iterator
from pathlib import Path
from types import SimpleNamespace
from typing import Any
from unittest.mock import MagicMock

import pytest

from app.config import Settings, get_settings
from app.services.llm_service import LLMService
from app.services.session_store import clear_store


def make_chat_response(content: str) -> Any:
    return SimpleNamespace(
        choices=[SimpleNamespace(message=SimpleNamespace(content=content))]
    )


@pytest.fixture
def mock_client() -> MagicMock:
    client = MagicMock()
    client.chat.completions.create.return_value = make_chat_response("ok")
    return client


@pytest.fixture
# test_settings - settings stub with a fake API key for LLMService
def test_settings() -> Settings:
    return Settings.model_construct(
        openai_api_key="test-key",
        openai_model="gpt-4o-mini",
        llm_temperature=0.0,
        mcp_server_url="http://127.0.0.1:8000/mcp",
    )


@pytest.fixture
def llm_service(test_settings: Settings, mock_client: MagicMock) -> LLMService:
    return LLMService(settings=test_settings, client=mock_client)


@pytest.fixture
def session_store_file(tmp_path: Path, monkeypatch) -> Path:
    path = tmp_path / "session_store.json"
    monkeypatch.setattr("app.services.session_store.SESSION_STORE_PATH", path)
    monkeypatch.setattr("app.config.SESSION_STORE_PATH", path)
    clear_store(path)
    return path


@pytest.fixture(autouse=True)
def clear_settings_cache() -> Iterator[None]:
    get_settings.cache_clear()
    yield
    get_settings.cache_clear()
