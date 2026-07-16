"""Integration tests: endpoint -> real service -> mocked upstream HTTP."""

from unittest.mock import AsyncMock, MagicMock, patch

import httpx
from fastapi.testclient import TestClient

from app.config import Settings
from app.dependencies import get_joke_service, get_weather_service
from app.main import app
from app.services.joke_service import JokeService
from app.services.weather_service import WeatherService


# test_weather_full_stack_with_mocked_upstream - test weather flow from endpoint through service to mocked HTTP
def test_weather_full_stack_with_mocked_upstream(client: TestClient) -> None:
    settings = Settings.model_construct(openweather_api_key="integration-key")
    app.dependency_overrides[get_weather_service] = lambda: WeatherService(settings)

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "name": "Mumbai",
        "main": {"temp": 30.5},
        "weather": [{"description": "haze"}],
    }

    with patch(
        "app.services.weather_service.httpx.AsyncClient",
    ) as mock_client_cls:
        mock_client = AsyncMock()
        mock_client.__aenter__.return_value = mock_client
        mock_client.get = AsyncMock(return_value=mock_response)
        mock_client_cls.return_value = mock_client

        response = client.get("/weather", params={"city": "Mumbai"})

    assert response.status_code == 200
    assert response.json() == {
        "city": "Mumbai",
        "temp_c": 30.5,
        "conditions": "haze",
    }


# test_joke_full_stack_with_mocked_upstream - test joke flow from endpoint through service to mocked HTTP
def test_joke_full_stack_with_mocked_upstream(client: TestClient) -> None:
    settings = Settings.model_construct(openweather_api_key="unused")
    app.dependency_overrides[get_joke_service] = lambda: JokeService(settings)

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "error": False,
        "type": "single",
        "joke": "Full stack joke.",
    }

    with patch(
        "app.services.joke_service.httpx.AsyncClient",
    ) as mock_client_cls:
        mock_client = AsyncMock()
        mock_client.__aenter__.return_value = mock_client
        mock_client.get = AsyncMock(return_value=mock_response)
        mock_client_cls.return_value = mock_client

        response = client.get("/joke")

    assert response.status_code == 200
    assert response.json()["setup"] == "Full stack joke."
    assert response.json()["delivery"] == ""


# test_weather_full_stack_unknown_city_propagates_404 - test that unknown cities propagate 404 through the stack
def test_weather_full_stack_unknown_city_propagates_404(client: TestClient) -> None:
    settings = Settings.model_construct(openweather_api_key="integration-key")
    app.dependency_overrides[get_weather_service] = lambda: WeatherService(settings)

    mock_response = MagicMock()
    mock_response.status_code = 404

    with patch("app.services.weather_service.httpx.AsyncClient") as mock_client_cls:
        mock_client = AsyncMock()
        mock_client.__aenter__.return_value = mock_client
        mock_client.get = AsyncMock(return_value=mock_response)
        mock_client_cls.return_value = mock_client

        response = client.get("/weather", params={"city": "NotARealCity"})

    assert response.status_code == 404


# test_weather_full_stack_unreachable_returns_502 - test that unreachable upstream returns 502 through the stack
def test_weather_full_stack_unreachable_returns_502(client: TestClient) -> None:
    settings = Settings.model_construct(openweather_api_key="integration-key")
    app.dependency_overrides[get_weather_service] = lambda: WeatherService(settings)

    with patch("app.services.weather_service.httpx.AsyncClient") as mock_client_cls:
        mock_client = AsyncMock()
        mock_client.__aenter__.return_value = mock_client
        mock_client.get = AsyncMock(side_effect=httpx.RequestError("down"))
        mock_client_cls.return_value = mock_client

        response = client.get("/weather", params={"city": "London"})

    assert response.status_code == 502
