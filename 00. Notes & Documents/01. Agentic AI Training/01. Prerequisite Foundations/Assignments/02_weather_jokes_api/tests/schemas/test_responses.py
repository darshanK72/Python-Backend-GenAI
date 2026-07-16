"""Tests for Pydantic response schemas."""

import pytest
from pydantic import ValidationError

from app.schemas.responses import HealthResponse, JokeResponse, WeatherResponse


# test_health_response_serialises - test that HealthResponse serialises to a status field
def test_health_response_serialises() -> None:
    model = HealthResponse(status="ok")
    assert model.model_dump() == {"status": "ok"}


# test_weather_response_requires_all_fields - test that WeatherResponse requires all fields
def test_weather_response_requires_all_fields() -> None:
    model = WeatherResponse(city="London", temp_c=12.4, conditions="rain")
    assert model.city == "London"
    assert model.temp_c == 12.4


# test_weather_response_rejects_missing_fields - test that WeatherResponse rejects missing fields
def test_weather_response_rejects_missing_fields() -> None:
    with pytest.raises(ValidationError):
        WeatherResponse(city="London", temp_c=12.4)  # type: ignore[call-arg]


# test_weather_response_coerces_numeric_temp - test that WeatherResponse coerces integer temps to float
def test_weather_response_coerces_numeric_temp() -> None:
    model = WeatherResponse(city="London", temp_c=12, conditions="rain")
    assert model.temp_c == 12.0


# test_joke_response_allows_empty_delivery - test that JokeResponse allows an empty delivery field
def test_joke_response_allows_empty_delivery() -> None:
    model = JokeResponse(setup="One liner", delivery="")
    assert model.delivery == ""


# test_joke_response_rejects_missing_setup - test that JokeResponse rejects a missing setup field
def test_joke_response_rejects_missing_setup() -> None:
    with pytest.raises(ValidationError):
        JokeResponse(delivery="punchline")  # type: ignore[call-arg]
