"""Unit tests for JokeService."""

import asyncio
from unittest.mock import AsyncMock, MagicMock

import httpx
import pytest
from fastapi import HTTPException

from app.config import Settings
from app.services.joke_service import JokeService
from tests.services.conftest import build_async_http_client


# test_normalise_joke_twopart - test that _normalise_joke maps twopart jokes correctly
def test_normalise_joke_twopart() -> None:
    joke = JokeService._normalise_joke(
        {"type": "twopart", "setup": "Why?", "delivery": "Because."},
    )
    assert joke.setup == "Why?"
    assert joke.delivery == "Because."


# test_normalise_joke_single_line - test that _normalise_joke maps single-line jokes correctly
def test_normalise_joke_single_line() -> None:
    joke = JokeService._normalise_joke({"type": "single", "joke": "A one-liner."})
    assert joke.setup == "A one-liner."
    assert joke.delivery == ""


# test_normalise_joke_handles_missing_fields - test that _normalise_joke handles missing fields safely
def test_normalise_joke_handles_missing_fields() -> None:
    joke = JokeService._normalise_joke({"type": "twopart"})
    assert joke.setup == ""
    assert joke.delivery == ""


# test_get_joke_maps_twopart_payload - test that get_joke maps twopart upstream payloads
def test_get_joke_maps_twopart_payload(
    joke_service: JokeService,
    mock_joke_twopart_response,
) -> None:
    client = build_async_http_client(AsyncMock(return_value=mock_joke_twopart_response))

    result = asyncio.run(joke_service.get_joke(client=client))

    assert result.setup == "Why did the developer go broke?"
    assert "cache" in result.delivery


# test_get_joke_maps_single_line_payload - test that get_joke maps single-line upstream payloads
def test_get_joke_maps_single_line_payload(
    joke_service: JokeService,
    mock_joke_single_response,
) -> None:
    client = build_async_http_client(AsyncMock(return_value=mock_joke_single_response))

    result = asyncio.run(joke_service.get_joke(client=client))

    assert result.setup == "A one-liner joke."
    assert result.delivery == ""


# test_get_joke_calls_configured_jokeapi_url - test that get_joke calls the configured JokeAPI URL
def test_get_joke_calls_configured_jokeapi_url(settings: Settings) -> None:
    settings = Settings.model_construct(jokeapi_url="https://example.test/joke")
    service = JokeService(settings)

    response = MagicMock()
    response.status_code = 200
    response.json.return_value = {"error": False, "type": "single", "joke": "Hi"}
    get_mock = AsyncMock(return_value=response)
    client = build_async_http_client(get_mock)

    asyncio.run(service.get_joke(client=client))

    assert get_mock.await_args.args[0] == "https://example.test/joke"


# test_get_joke_upstream_non_200_returns_502 - test that non-200 upstream responses return 502
def test_get_joke_upstream_non_200_returns_502(joke_service: JokeService) -> None:
    response = MagicMock()
    response.status_code = 503
    client = build_async_http_client(AsyncMock(return_value=response))

    with pytest.raises(HTTPException) as exc_info:
        asyncio.run(joke_service.get_joke(client=client))

    assert exc_info.value.status_code == 502
    assert "unexpected error" in exc_info.value.detail.lower()


# test_get_joke_error_flag_in_payload_returns_502 - test that upstream error flags return 502
def test_get_joke_error_flag_in_payload_returns_502(joke_service: JokeService) -> None:
    response = MagicMock()
    response.status_code = 200
    response.json.return_value = {"error": True, "message": "Rate limit hit"}
    client = build_async_http_client(AsyncMock(return_value=response))

    with pytest.raises(HTTPException) as exc_info:
        asyncio.run(joke_service.get_joke(client=client))

    assert exc_info.value.status_code == 502
    assert exc_info.value.detail == "Rate limit hit"


# test_get_joke_error_flag_without_message_uses_default - test that error flags without a message use the default detail
def test_get_joke_error_flag_without_message_uses_default(joke_service: JokeService) -> None:
    response = MagicMock()
    response.status_code = 200
    response.json.return_value = {"error": True}
    client = build_async_http_client(AsyncMock(return_value=response))

    with pytest.raises(HTTPException) as exc_info:
        asyncio.run(joke_service.get_joke(client=client))

    assert exc_info.value.detail == "Joke service error."


# test_get_joke_unreachable_upstream_returns_502 - test that unreachable upstream returns 502
def test_get_joke_unreachable_upstream_returns_502(joke_service: JokeService) -> None:
    client = build_async_http_client(
        AsyncMock(side_effect=httpx.RequestError("connection failed")),
    )

    with pytest.raises(HTTPException) as exc_info:
        asyncio.run(joke_service.get_joke(client=client))

    assert exc_info.value.status_code == 502
    assert "unreachable" in exc_info.value.detail.lower()
