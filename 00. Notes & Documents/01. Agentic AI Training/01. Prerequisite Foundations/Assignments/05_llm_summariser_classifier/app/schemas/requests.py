"""API request models."""

from __future__ import annotations

from pydantic import BaseModel, Field


class TextRequest(BaseModel):
    """Request body containing text for summarise or classify."""

    text: str = Field(min_length=1)
