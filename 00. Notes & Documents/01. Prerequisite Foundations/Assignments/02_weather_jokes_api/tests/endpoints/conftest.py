"""Endpoint-layer test helpers."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

from app.dependencies import get_joke_service, get_weather_service
from app.main import app
from app.schemas.responses import JokeResponse, WeatherResponse
from app.services.joke_service import JokeService
from app.services.weather_service import WeatherService


def override_weather_service(return_value: WeatherResponse | Exception) -> None:
    mock_service = MagicMock(spec=WeatherService)
    if isinstance(return_value, Exception):
        mock_service.get_weather = AsyncMock(side_effect=return_value)
    else:
        mock_service.get_weather = AsyncMock(return_value=return_value)
    app.dependency_overrides[get_weather_service] = lambda: mock_service


def override_joke_service(return_value: JokeResponse | Exception) -> None:
    mock_service = MagicMock(spec=JokeService)
    if isinstance(return_value, Exception):
        mock_service.get_joke = AsyncMock(side_effect=return_value)
    else:
        mock_service.get_joke = AsyncMock(return_value=return_value)
    app.dependency_overrides[get_joke_service] = lambda: mock_service
