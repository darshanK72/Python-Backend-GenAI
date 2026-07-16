"""Shared pytest fixtures for Weather & Jokes API tests."""

from __future__ import annotations

from collections.abc import Iterator
from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient

from app.config import Settings, get_settings
from app.dependencies import get_joke_service, get_weather_service
from app.main import app
from app.services.joke_service import JokeService
from app.services.weather_service import WeatherService


# settings - return isolated settings without reading the developer's real .env
@pytest.fixture
def settings() -> Settings:
    """Isolated settings without reading the developer's real .env."""
    return Settings.model_construct(
        openweather_api_key="test-openweather-key",
        app_title="Weather & Jokes API Test",
        app_debug=True,
    )


# client - return a FastAPI test client for the application
@pytest.fixture
def client() -> Iterator[TestClient]:
    with TestClient(app) as test_client:
        yield test_client


# reset_app_state - clear dependency overrides and settings cache between tests
@pytest.fixture(autouse=True)
def reset_app_state() -> Iterator[None]:
    """Clear dependency overrides and settings cache between tests."""
    app.dependency_overrides.clear()
    get_settings.cache_clear()
    get_weather_service.cache_clear()
    get_joke_service.cache_clear()
    yield
    app.dependency_overrides.clear()
    get_settings.cache_clear()
    get_weather_service.cache_clear()
    get_joke_service.cache_clear()


# weather_service - return a WeatherService wired to test settings
@pytest.fixture
def weather_service(settings: Settings) -> WeatherService:
    return WeatherService(settings)


# joke_service - return a JokeService wired to test settings
@pytest.fixture
def joke_service(settings: Settings) -> JokeService:
    return JokeService(settings)


# mock_weather_response - return a mocked successful OpenWeather HTTP response
@pytest.fixture
def mock_weather_response() -> MagicMock:
    response = MagicMock()
    response.status_code = 200
    response.json.return_value = {
        "name": "London",
        "main": {"temp": 12.4},
        "weather": [{"description": "light rain"}],
    }
    return response


# mock_joke_twopart_response - return a mocked successful twopart JokeAPI response
@pytest.fixture
def mock_joke_twopart_response() -> MagicMock:
    response = MagicMock()
    response.status_code = 200
    response.json.return_value = {
        "error": False,
        "type": "twopart",
        "setup": "Why did the developer go broke?",
        "delivery": "Because he used up all his cache.",
    }
    return response


# mock_joke_single_response - return a mocked successful single-line JokeAPI response
@pytest.fixture
def mock_joke_single_response() -> MagicMock:
    response = MagicMock()
    response.status_code = 200
    response.json.return_value = {
        "error": False,
        "type": "single",
        "joke": "A one-liner joke.",
    }
    return response
