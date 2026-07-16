"""FastAPI dependency injection helpers."""

from __future__ import annotations

from functools import lru_cache

from app.config import Settings, get_settings
from app.services.joke_service import JokeService
from app.services.weather_service import WeatherService


# get_weather_service - return a cached WeatherService instance
@lru_cache
def get_weather_service() -> WeatherService:
    return WeatherService(get_settings())


# get_joke_service - return a cached JokeService instance
@lru_cache
def get_joke_service() -> JokeService:
    return JokeService(get_settings())


# get_app_settings - return application settings for dependency injection
def get_app_settings() -> Settings:
    return get_settings()
