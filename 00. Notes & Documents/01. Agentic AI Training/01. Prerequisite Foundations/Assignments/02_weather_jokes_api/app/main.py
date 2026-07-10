"""FastAPI application entry point."""

from fastapi import FastAPI

from app.config import get_settings
from app.endpoints import health, jokes, weather

settings = get_settings()

app = FastAPI(
    title=settings.app_title,
    description=(
        "Internal gateway over OpenWeather and JokeAPI. "
        "MAS prerequisite foundation assignment 02."
    ),
    version="1.0.0",
    debug=settings.app_debug,
)

app.include_router(health.router)
app.include_router(weather.router)
app.include_router(jokes.router)
