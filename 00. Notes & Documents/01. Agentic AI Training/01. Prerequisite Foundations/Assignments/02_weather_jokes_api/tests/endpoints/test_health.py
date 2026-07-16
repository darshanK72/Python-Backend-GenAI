"""Tests for health endpoint and OpenAPI metadata."""

from fastapi.testclient import TestClient


# test_health_returns_ok - test that GET /health returns status ok
def test_health_returns_ok(client: TestClient) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


# test_openapi_lists_all_assignment_endpoints - test that OpenAPI lists all assignment endpoints
def test_openapi_lists_all_assignment_endpoints(client: TestClient) -> None:
    schema = client.get("/openapi.json").json()
    paths = schema["paths"]

    assert "/health" in paths
    assert "/weather" in paths
    assert "/joke" in paths


# test_openapi_documents_response_schemas - test that OpenAPI documents all response schemas
def test_openapi_documents_response_schemas(client: TestClient) -> None:
    schema = client.get("/openapi.json").json()
    components = schema["components"]["schemas"]

    assert "HealthResponse" in components
    assert "WeatherResponse" in components
    assert "JokeResponse" in components


# test_weather_endpoint_tagged_in_openapi - test that the weather endpoint is tagged and documents city
def test_weather_endpoint_tagged_in_openapi(client: TestClient) -> None:
    schema = client.get("/openapi.json").json()
    weather_get = schema["paths"]["/weather"]["get"]

    assert "weather" in weather_get["tags"]
    assert "city" in weather_get["parameters"][0]["name"]


# test_joke_endpoint_tagged_in_openapi - test that the joke endpoint is tagged in OpenAPI
def test_joke_endpoint_tagged_in_openapi(client: TestClient) -> None:
    schema = client.get("/openapi.json").json()
    joke_get = schema["paths"]["/joke"]["get"]

    assert "jokes" in joke_get["tags"]
