"""Shared pytest fixtures."""

from __future__ import annotations

from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient

from app.config import Settings, get_settings
from app.dependencies import get_note_store
from app.main import app


# api_key - return the test API key
@pytest.fixture
def api_key() -> str:
    return "test-key"


# auth_headers - return headers with the test API key
@pytest.fixture
def auth_headers(api_key: str) -> dict[str, str]:
    return {"X-API-Key": api_key}


# client - return a FastAPI test client for the application
@pytest.fixture
def client() -> Iterator[TestClient]:
    with TestClient(app) as test_client:
        yield test_client


# isolated_app_state - reset store and apply test API key before each test
@pytest.fixture(autouse=True)
def isolated_app_state(monkeypatch: pytest.MonkeyPatch) -> Iterator[None]:
    """Reset store and apply test API key before each test."""
    monkeypatch.setenv("NOTES_API_KEY", "test-key")
    get_settings.cache_clear()
    get_note_store().reset()
    app.dependency_overrides.clear()
    yield
    get_settings.cache_clear()
    get_note_store().reset()
    app.dependency_overrides.clear()


# test_settings - return isolated settings for dependency tests
@pytest.fixture
def test_settings() -> Settings:
    return Settings.model_construct(notes_api_key="test-key")
