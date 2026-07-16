"""Unit tests for WeatherService."""

import asyncio
from unittest.mock import AsyncMock, MagicMock

import httpx
import pytest
from fastapi import HTTPException

from app.config import Settings
from app.services.weather_service import WeatherService
from tests.services.conftest import build_async_http_client


# test_get_weather_maps_openweather_payload - test that get_weather maps OpenWeather payload fields
def test_get_weather_maps_openweather_payload(
    weather_service: WeatherService,
    mock_weather_response,
) -> None:
    client = build_async_http_client(AsyncMock(return_value=mock_weather_response))

    result = asyncio.run(weather_service.get_weather("London", client=client))

    assert result.city == "London"
    assert result.temp_c == 12.4
    assert result.conditions == "light rain"


# test_get_weather_sends_expected_query_params - test that get_weather sends expected query parameters
def test_get_weather_sends_expected_query_params(
    weather_service: WeatherService,
    mock_weather_response,
) -> None:
    get_mock = AsyncMock(return_value=mock_weather_response)
    client = build_async_http_client(get_mock)

    asyncio.run(weather_service.get_weather("London", client=client))

    get_mock.assert_awaited_once()
    call_kwargs = get_mock.await_args.kwargs
    assert call_kwargs["params"] == {
        "q": "London",
        "appid": "test-openweather-key",
        "units": "metric",
    }


# test_get_weather_uses_city_fallback_when_name_missing - test that get_weather falls back to the requested city name
def test_get_weather_uses_city_fallback_when_name_missing(
    weather_service: WeatherService,
) -> None:
    response = MagicMock()
    response.status_code = 200
    response.json.return_value = {
        "main": {"temp": 5.0},
        "weather": [{"description": "snow"}],
    }
    client = build_async_http_client(AsyncMock(return_value=response))

    result = asyncio.run(weather_service.get_weather("FallbackCity", client=client))

    assert result.city == "FallbackCity"
    assert result.temp_c == 5.0
    assert result.conditions == "snow"


# test_get_weather_unknown_city_returns_404 - test that get_weather returns 404 for unknown cities
def test_get_weather_unknown_city_returns_404(weather_service: WeatherService) -> None:
    response = MagicMock()
    response.status_code = 404
    client = build_async_http_client(AsyncMock(return_value=response))

    with pytest.raises(HTTPException) as exc_info:
        asyncio.run(weather_service.get_weather("NotARealCity", client=client))

    assert exc_info.value.status_code == 404
    assert "NotARealCity" in exc_info.value.detail


# test_get_weather_unexpected_upstream_status_returns_502 - test that unexpected upstream status returns 502
def test_get_weather_unexpected_upstream_status_returns_502(
    weather_service: WeatherService,
) -> None:
    response = MagicMock()
    response.status_code = 500
    client = build_async_http_client(AsyncMock(return_value=response))

    with pytest.raises(HTTPException) as exc_info:
        asyncio.run(weather_service.get_weather("London", client=client))

    assert exc_info.value.status_code == 502
    assert "unexpected error" in exc_info.value.detail.lower()


# test_get_weather_unreachable_upstream_returns_502 - test that unreachable upstream returns 502
def test_get_weather_unreachable_upstream_returns_502(weather_service: WeatherService) -> None:
    client = build_async_http_client(
        AsyncMock(side_effect=httpx.RequestError("connection failed")),
    )

    with pytest.raises(HTTPException) as exc_info:
        asyncio.run(weather_service.get_weather("London", client=client))

    assert exc_info.value.status_code == 502
    assert "unreachable" in exc_info.value.detail.lower()


# test_get_weather_missing_api_key_returns_502 - test that a missing API key returns 502
def test_get_weather_missing_api_key_returns_502() -> None:
    service = WeatherService(Settings.model_construct(openweather_api_key=""))

    with pytest.raises(HTTPException) as exc_info:
        asyncio.run(service.get_weather("London", client=AsyncMock()))

    assert exc_info.value.status_code == 502
    assert "not configured" in exc_info.value.detail.lower()


# test_get_weather_uses_configured_openweather_url - test that get_weather uses the configured OpenWeather URL
def test_get_weather_uses_configured_openweather_url(settings: Settings) -> None:
    settings = Settings.model_construct(
        openweather_api_key="test-key",
        openweather_url="https://example.test/weather",
    )
    service = WeatherService(settings)

    response = MagicMock()
    response.status_code = 200
    response.json.return_value = {
        "name": "Berlin",
        "main": {"temp": 1.0},
        "weather": [{"description": "clouds"}],
    }
    get_mock = AsyncMock(return_value=response)
    client = build_async_http_client(get_mock)

    asyncio.run(service.get_weather("Berlin", client=client))

    assert get_mock.await_args.args[0] == "https://example.test/weather"
