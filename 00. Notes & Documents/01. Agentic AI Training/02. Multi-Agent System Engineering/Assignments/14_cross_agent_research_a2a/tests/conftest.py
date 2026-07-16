"""Shared pytest fixtures."""

from __future__ import annotations

from collections.abc import Iterator
from types import SimpleNamespace
from typing import Any
from unittest.mock import MagicMock

import pytest

from app.config import Settings, get_settings
from app.services.llm_service import LLMService
from app.services.task_store import clear_tasks

# SAMPLE_RESEARCH - structured ResearchAgent output used across tests
SAMPLE_RESEARCH = """3 Key Facts:
1. Event-driven systems decouple producers and consumers.
2. Messages are stored in durable logs before processing.
3. Consumers process events asynchronously at their own pace.
2 Current Trends:
1. Cloud-native event buses are replacing self-hosted brokers.
2. Schema registries are standard for contract testing.
1 Notable Challenge: Ordering guarantees are hard across service boundaries."""

# SAMPLE_ARTICLE - sample writer brief that references research facts
SAMPLE_ARTICLE = """Introduction
Event-driven architecture helps teams scale async workflows across services.

Main Body
As noted in the research, producers and consumers are decoupled through durable logs.
Cloud-native event buses are increasingly replacing self-hosted brokers in production.

Conclusion
Teams adopting event-driven patterns should plan for ordering challenges early."""


# make_chat_response - build a mocked chat completion response namespace
def make_chat_response(content: str) -> Any:
    return SimpleNamespace(
        choices=[SimpleNamespace(message=SimpleNamespace(content=content))]
    )


# mock_client - injectable MagicMock OpenAI client
@pytest.fixture
def mock_client() -> MagicMock:
    client = MagicMock()
    client.chat.completions.create.return_value = make_chat_response(SAMPLE_RESEARCH)
    return client


# test_settings - Settings constructed without reading the real environment
@pytest.fixture
def test_settings() -> Settings:
    return Settings.model_construct(
        openai_api_key="test-key",
        openai_model="gpt-4o-mini",
        llm_temperature=0.0,
        research_agent_url="http://localhost:8001",
    )


# llm_service - LLMService wired to mocked settings and client
@pytest.fixture
def llm_service(test_settings: Settings, mock_client: MagicMock) -> LLMService:
    return LLMService(settings=test_settings, client=mock_client)


# mock_http_client - fake httpx client returning AgentCard and task results
@pytest.fixture
def mock_http_client():
    card = {
        "name": "ResearchAgent",
        "version": "1.0",
        "description": "Research service",
        "url": "http://localhost:8001",
        "skills": [{"name": "research", "description": "Research topics"}],
    }

    class FakeResponse:
        def __init__(self, payload: dict, status_code: int = 200):
            self._payload = payload
            self.status_code = status_code

        def raise_for_status(self) -> None:
            if self.status_code >= 400:
                raise RuntimeError("http error")

        def json(self) -> dict:
            return self._payload

    class FakeHttp:
        def get(self, url: str, **kwargs):
            return FakeResponse(card)

        def post(self, url: str, **kwargs):
            return FakeResponse(
                {
                    "id": kwargs["json"]["id"],
                    "status": "completed",
                    "output": SAMPLE_RESEARCH,
                }
            )

        def close(self) -> None:
            return None

    return FakeHttp()


# reset_task_store - clear in-memory A2A task store around each test
@pytest.fixture(autouse=True)
def reset_task_store() -> Iterator[None]:
    clear_tasks()
    yield
    clear_tasks()


# clear_settings_cache - clear get_settings LRU cache around each test
@pytest.fixture(autouse=True)
def clear_settings_cache() -> Iterator[None]:
    get_settings.cache_clear()
    yield
    get_settings.cache_clear()
