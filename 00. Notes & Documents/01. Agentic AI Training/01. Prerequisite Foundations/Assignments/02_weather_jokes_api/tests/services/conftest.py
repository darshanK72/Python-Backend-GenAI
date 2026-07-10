"""Service-layer test helpers."""

from __future__ import annotations

from unittest.mock import AsyncMock

import httpx


def build_async_http_client(get_mock: AsyncMock) -> AsyncMock:
    """Return a mock httpx.AsyncClient whose .get is the provided coroutine mock."""
    client = AsyncMock(spec=httpx.AsyncClient)
    client.get = get_mock
    return client
