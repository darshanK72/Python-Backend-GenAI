"""Shared pytest fixtures."""

from __future__ import annotations

from collections.abc import Iterator
from types import SimpleNamespace
from typing import Any
from unittest.mock import MagicMock

import pytest
from langchain_core.documents import Document

from app.config import Settings, get_settings
from app.services.llm_service import LLMService
from app.services.vector_store import VectorStore


# make_chat_response - build a minimal OpenAI-style chat completion response
def make_chat_response(content: str) -> Any:
    return SimpleNamespace(
        choices=[SimpleNamespace(message=SimpleNamespace(content=content))]
    )


# mock_client - provide a mocked OpenAI chat client
@pytest.fixture
def mock_client() -> MagicMock:
    client = MagicMock()
    client.chat.completions.create.return_value = make_chat_response("relevant")
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


# mock_store - provide an in-memory FAISS double for retrieval tests
@pytest.fixture
def mock_store() -> VectorStore:
    chunks = {
        "trunk": [
            Document(
                page_content="Trunk-based development keeps one main branch.",
                metadata={"doc_title": "Continuous integration", "chunk_index": 0},
            ),
            Document(
                page_content="Federal Reserve sets interest rates monthly.",
                metadata={"doc_title": "Economics", "chunk_index": 0},
            ),
        ],
        "debt": [
            Document(
                page_content="Technical debt accumulates when teams defer refactoring.",
                metadata={"doc_title": "Technical debt", "chunk_index": 0},
            ),
        ],
        "microservices": [
            Document(
                page_content="Microservices split systems into independently deployable services.",
                metadata={"doc_title": "Microservices", "chunk_index": 0},
            ),
            Document(
                page_content="Monoliths keep all modules in one deployable unit.",
                metadata={"doc_title": "Software engineering", "chunk_index": 1},
            ),
        ],
        "fed": [
            Document(
                page_content="The Federal Reserve adjusts interest rates to manage inflation.",
                metadata={"doc_title": "Economics", "chunk_index": 1},
            ),
        ],
    }

    class FakeStore:
        def similarity_search(self, query: str, k: int = 4) -> list[Document]:
            lowered = query.lower()
            if "federal reserve" in lowered or "interest rates" in lowered:
                return chunks["fed"][:k]
            if "technical debt" in lowered:
                return chunks["debt"][:k]
            if "microservices" in lowered and "monolith" in lowered:
                return chunks["microservices"][:k]
            if "trunk-based" in lowered:
                return chunks["trunk"][:k]
            return chunks["trunk"][:k]

    return VectorStore(FakeStore())  # type: ignore[arg-type]


# clear_settings_cache - reset the cached settings singleton between tests
@pytest.fixture(autouse=True)
def clear_settings_cache() -> Iterator[None]:
    get_settings.cache_clear()
    yield
    get_settings.cache_clear()
