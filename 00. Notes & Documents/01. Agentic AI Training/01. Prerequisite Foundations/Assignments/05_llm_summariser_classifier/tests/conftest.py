"""Shared pytest fixtures."""

from __future__ import annotations

from collections.abc import Iterator
from types import SimpleNamespace
from typing import Any
from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient

from app.config import Settings, get_settings
from app.dependencies import get_llm_service
from app.main import app
from app.schemas.llm import ClassifyResult, SummariseResult
from app.services.llm_service import LLMService


def make_chat_response(content: str) -> Any:
    return SimpleNamespace(
        choices=[SimpleNamespace(message=SimpleNamespace(content=content))],
        usage=SimpleNamespace(prompt_tokens=10, completion_tokens=5),
    )


@pytest.fixture
def api_key() -> str:
    return "test-key"


@pytest.fixture
def auth_headers(api_key: str) -> dict[str, str]:
    return {"X-API-Key": api_key}


@pytest.fixture
def test_settings() -> Settings:
    return Settings.model_construct(
        llm_service_api_key="test-key",
        openai_api_key="sk-test",
        openai_model="gpt-4o-mini",
        llm_temperature=0.0,
    )


@pytest.fixture
def mock_client() -> MagicMock:
    client = MagicMock()
    client.chat.completions.create.return_value = make_chat_response("plain text")
    return client


@pytest.fixture
def llm_service(test_settings: Settings, mock_client: MagicMock) -> LLMService:
    return LLMService(settings=test_settings, client=mock_client)


@pytest.fixture
def client(llm_service: LLMService) -> Iterator[TestClient]:
    app.dependency_overrides[get_llm_service] = lambda: llm_service
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


@pytest.fixture(autouse=True)
def isolated_app_state(monkeypatch: pytest.MonkeyPatch) -> Iterator[None]:
    monkeypatch.setenv("LLM_SERVICE_API_KEY", "test-key")
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test")
    get_settings.cache_clear()
    get_llm_service.cache_clear()
    app.dependency_overrides.clear()
    yield
    get_settings.cache_clear()
    get_llm_service.cache_clear()
    app.dependency_overrides.clear()


@pytest.fixture
def sample_summarise_result() -> SummariseResult:
    return SummariseResult(summary="Short summary.", word_count=2)


@pytest.fixture
def sample_classify_result() -> ClassifyResult:
    return ClassifyResult(
        category="bug",
        confidence=0.92,
        rationale="Describes a reproducible crash.",
    )
