"""Tests for health endpoint and OpenAPI metadata."""

from fastapi.testclient import TestClient


# test_health_returns_ok - test that GET /health returns status ok
def test_health_returns_ok(client: TestClient) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


# test_openapi_lists_assignment_endpoints - test that OpenAPI lists all assignment endpoints
def test_openapi_lists_assignment_endpoints(client: TestClient) -> None:
    schema = client.get("/openapi.json").json()
    paths = schema["paths"]

    assert "/health" in paths
    assert "/summarise" in paths
    assert "/classify" in paths


# test_openapi_documents_response_schemas - test that OpenAPI documents all response schemas
def test_openapi_documents_response_schemas(client: TestClient) -> None:
    schema = client.get("/openapi.json").json()
    components = schema["components"]["schemas"]

    assert "HealthResponse" in components
    assert "SummariseResult" in components
    assert "ClassifyResult" in components
    assert "TextRequest" in components
