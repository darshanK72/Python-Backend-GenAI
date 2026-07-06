"""Weather endpoints."""

from fastapi import APIRouter, Depends, Query

from app.dependencies import get_weather_service
from app.schemas.responses import WeatherResponse
from app.services.weather_service import WeatherService

router = APIRouter(prefix="/weather", tags=["weather"])


@router.get("", response_model=WeatherResponse)
async def get_weather(
    city: str = Query(..., min_length=1, description="City name"),
    service: WeatherService = Depends(get_weather_service),
) -> WeatherResponse:
    """Return current weather for a city via OpenWeather."""
    return await service.get_weather(city)
