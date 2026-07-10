"""Tests for GET /joke endpoint."""

from fastapi import HTTPException
from fastapi.testclient import TestClient

from app.schemas.responses import JokeResponse
from tests.endpoints.conftest import override_joke_service


def test_joke_returns_typed_twopart_response(client: TestClient) -> None:
    override_joke_service(
        JokeResponse(
            setup="Why did the developer go broke?",
            delivery="Because he used up all his cache.",
        ),
    )

    response = client.get("/joke")
    assert response.status_code == 200
    assert response.json() == {
        "setup": "Why did the developer go broke?",
        "delivery": "Because he used up all his cache.",
    }


def test_joke_returns_single_line_normalised_shape(client: TestClient) -> None:
    override_joke_service(JokeResponse(setup="A one-liner joke.", delivery=""))

    response = client.get("/joke")
    assert response.status_code == 200
    assert response.json()["setup"] == "A one-liner joke."
    assert response.json()["delivery"] == ""


def test_joke_upstream_unreachable_returns_502(client: TestClient) -> None:
    override_joke_service(
        HTTPException(status_code=502, detail="Joke service is unreachable."),
    )

    response = client.get("/joke")
    assert response.status_code == 502
    assert "unreachable" in response.json()["detail"].lower()


def test_joke_upstream_error_payload_returns_502(client: TestClient) -> None:
    override_joke_service(
        HTTPException(status_code=502, detail="Joke service error."),
    )

    response = client.get("/joke")
    assert response.status_code == 502


def test_joke_response_matches_pydantic_schema(client: TestClient) -> None:
    override_joke_service(JokeResponse(setup="Setup", delivery="Delivery"))

    response = client.get("/joke")
    payload = response.json()

    assert set(payload.keys()) == {"setup", "delivery"}
    assert isinstance(payload["setup"], str)
    assert isinstance(payload["delivery"], str)
