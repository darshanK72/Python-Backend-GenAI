"""API response schemas."""

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str = Field(examples=["ok"])


class WeatherResponse(BaseModel):
    city: str
    temp_c: float
    conditions: str


class JokeResponse(BaseModel):
    setup: str
    delivery: str
