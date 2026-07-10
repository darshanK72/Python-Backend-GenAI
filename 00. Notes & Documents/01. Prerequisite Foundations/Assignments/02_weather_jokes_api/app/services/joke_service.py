"""JokeAPI upstream client."""

from __future__ import annotations

from typing import Any

import httpx
from fastapi import HTTPException

from app.config import Settings, get_settings
from app.schemas.responses import JokeResponse


class JokeService:
    """Fetches and normalises jokes from JokeAPI."""

    def __init__(self, settings: Settings | None = None) -> None:
        self.settings = settings or get_settings()

    async def get_joke(self, *, client: httpx.AsyncClient | None = None) -> JokeResponse:
        """Return a random joke in a consistent setup/delivery shape."""
        response = await self._request(client=client)

        if response.status_code != 200:
            raise HTTPException(status_code=502, detail="Joke service returned an unexpected error.")

        payload = response.json()
        if payload.get("error"):
            raise HTTPException(
                status_code=502,
                detail=payload.get("message", "Joke service error."),
            )

        return self._normalise_joke(payload)

    @staticmethod
    def _normalise_joke(payload: dict[str, Any]) -> JokeResponse:
        if payload.get("type") == "twopart":
            return JokeResponse(
                setup=payload.get("setup", ""),
                delivery=payload.get("delivery", ""),
            )
        joke = payload.get("joke", "")
        return JokeResponse(setup=joke, delivery="")

    async def _request(self, *, client: httpx.AsyncClient | None) -> httpx.Response:
        if client is not None:
            try:
                return await client.get(self.settings.jokeapi_url)
            except httpx.RequestError:
                raise HTTPException(status_code=502, detail="Joke service is unreachable.") from None

        try:
            async with httpx.AsyncClient(timeout=self.settings.http_timeout_seconds) as session:
                return await session.get(self.settings.jokeapi_url)
        except httpx.RequestError:
            raise HTTPException(status_code=502, detail="Joke service is unreachable.") from None
