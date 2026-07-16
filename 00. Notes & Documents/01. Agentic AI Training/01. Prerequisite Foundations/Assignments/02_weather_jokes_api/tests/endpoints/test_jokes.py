"""Tests for GET /joke endpoint."""

from fastapi import HTTPException
from fastapi.testclient import TestClient

from app.schemas.responses import JokeResponse
from tests.endpoints.conftest import override_joke_service


# test_joke_returns_typed_twopart_response - test that GET /joke returns a twopart joke response
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


# test_joke_returns_single_line_normalised_shape - test that single-line jokes use an empty delivery field
def test_joke_returns_single_line_normalised_shape(client: TestClient) -> None:
    override_joke_service(JokeResponse(setup="A one-liner joke.", delivery=""))

    response = client.get("/joke")
    assert response.status_code == 200
    assert response.json()["setup"] == "A one-liner joke."
    assert response.json()["delivery"] == ""


# test_joke_upstream_unreachable_returns_502 - test that unreachable upstream returns 502
def test_joke_upstream_unreachable_returns_502(client: TestClient) -> None:
    override_joke_service(
        HTTPException(status_code=502, detail="Joke service is unreachable."),
    )

    response = client.get("/joke")
    assert response.status_code == 502
    assert "unreachable" in response.json()["detail"].lower()


# test_joke_upstream_error_payload_returns_502 - test that upstream error payloads return 502
def test_joke_upstream_error_payload_returns_502(client: TestClient) -> None:
    override_joke_service(
        HTTPException(status_code=502, detail="Joke service error."),
    )

    response = client.get("/joke")
    assert response.status_code == 502


# test_joke_response_matches_pydantic_schema - test that GET /joke returns setup and delivery strings
def test_joke_response_matches_pydantic_schema(client: TestClient) -> None:
    override_joke_service(JokeResponse(setup="Setup", delivery="Delivery"))

    response = client.get("/joke")
    payload = response.json()

    assert set(payload.keys()) == {"setup", "delivery"}
    assert isinstance(payload["setup"], str)
    assert isinstance(payload["delivery"], str)
