"""Tests for GET /weather endpoint."""

from fastapi import HTTPException
from fastapi.testclient import TestClient

from app.schemas.responses import WeatherResponse
from tests.endpoints.conftest import override_weather_service


def test_weather_requires_city_query_param(client: TestClient) -> None:
    response = client.get("/weather")
    assert response.status_code == 422


def test_weather_rejects_empty_city(client: TestClient) -> None:
    response = client.get("/weather", params={"city": ""})
    assert response.status_code == 422


def test_weather_returns_typed_response(client: TestClient) -> None:
    override_weather_service(
        WeatherResponse(city="London", temp_c=12.4, conditions="light rain"),
    )

    response = client.get("/weather", params={"city": "London"})
    assert response.status_code == 200
    assert response.json() == {
        "city": "London",
        "temp_c": 12.4,
        "conditions": "light rain",
    }


def test_weather_unknown_city_returns_404(client: TestClient) -> None:
    override_weather_service(HTTPException(status_code=404, detail="City not found: NotARealCity"))

    response = client.get("/weather", params={"city": "NotARealCity"})
    assert response.status_code == 404
    assert response.json()["detail"] == "City not found: NotARealCity"


def test_weather_upstream_unreachable_returns_502(client: TestClient) -> None:
    override_weather_service(
        HTTPException(status_code=502, detail="Weather service is unreachable."),
    )

    response = client.get("/weather", params={"city": "London"})
    assert response.status_code == 502
    assert "unreachable" in response.json()["detail"].lower()


def test_weather_missing_api_key_returns_502(client: TestClient) -> None:
    override_weather_service(
        HTTPException(status_code=502, detail="OpenWeather API key is not configured."),
    )

    response = client.get("/weather", params={"city": "London"})
    assert response.status_code == 502
    assert "not configured" in response.json()["detail"].lower()


def test_weather_response_matches_pydantic_schema(client: TestClient) -> None:
    override_weather_service(
        WeatherResponse(city="Paris", temp_c=18.0, conditions="clear sky"),
    )

    response = client.get("/weather", params={"city": "Paris"})
    payload = response.json()

    assert set(payload.keys()) == {"city", "temp_c", "conditions"}
    assert isinstance(payload["temp_c"], float)
