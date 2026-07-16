"""LLM response models."""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator

# ALLOWED_CATEGORIES - valid classification categories returned by POST /classify
ALLOWED_CATEGORIES = frozenset({"bug", "feature", "question", "feedback"})


class SummariseResult(BaseModel):
    """Structured summary returned by POST /summarise."""

    summary: str
    word_count: int = Field(ge=0)


class ClassifyResult(BaseModel):
    """Structured classification returned by POST /classify."""

    category: str
    confidence: float = Field(ge=0.0, le=1.0)
    rationale: str

    # validate_category - normalise and validate the classification category
    @field_validator("category")
    @classmethod
    def validate_category(cls, value: str) -> str:
        normalised = value.strip().lower()
        if normalised not in ALLOWED_CATEGORIES:
            raise ValueError(f"Category must be one of {sorted(ALLOWED_CATEGORIES)}.")
        return normalised
