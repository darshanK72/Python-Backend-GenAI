"""API response schemas."""

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """Health check response payload."""

    status: str = Field(examples=["ok"])


class WeatherResponse(BaseModel):
    """Trimmed weather data returned by GET /weather."""

    city: str
    temp_c: float
    conditions: str


class JokeResponse(BaseModel):
    """Normalised joke payload returned by GET /joke."""

    setup: str
    delivery: str
