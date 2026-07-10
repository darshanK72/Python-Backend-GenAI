"""OpenWeather upstream client."""

from __future__ import annotations

import httpx
from fastapi import HTTPException

from app.config import Settings, get_settings
from app.schemas.responses import WeatherResponse


class WeatherService:
    """Fetches and maps weather data from OpenWeather."""

    def __init__(self, settings: Settings | None = None) -> None:
        self.settings = settings or get_settings()

    async def get_weather(
        self,
        city: str,
        *,
        client: httpx.AsyncClient | None = None,
    ) -> WeatherResponse:
        """Return trimmed weather data for a city."""
        api_key = self.settings.openweather_api_key
        if not api_key:
            raise HTTPException(status_code=502, detail="OpenWeather API key is not configured.")

        params = {"q": city, "appid": api_key, "units": "metric"}
        response = await self._request(params=params, client=client)

        if response.status_code == 404:
            raise HTTPException(status_code=404, detail=f"City not found: {city}")
        if response.status_code != 200:
            raise HTTPException(status_code=502, detail="Weather service returned an unexpected error.")

        payload = response.json()
        return WeatherResponse(
            city=payload.get("name", city),
            temp_c=float(payload["main"]["temp"]),
            conditions=payload["weather"][0]["description"],
        )

    async def _request(
        self,
        *,
        params: dict[str, str],
        client: httpx.AsyncClient | None,
    ) -> httpx.Response:
        if client is not None:
            try:
                return await client.get(self.settings.openweather_url, params=params)
            except httpx.RequestError:
                raise HTTPException(status_code=502, detail="Weather service is unreachable.") from None

        try:
            async with httpx.AsyncClient(timeout=self.settings.http_timeout_seconds) as session:
                return await session.get(self.settings.openweather_url, params=params)
        except httpx.RequestError:
            raise HTTPException(status_code=502, detail="Weather service is unreachable.") from None
