"""Tests for Pydantic LLM schemas."""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from app.schemas.llm import ClassifyResult, SummariseResult


def test_classify_result_normalises_category() -> None:
    result = ClassifyResult(category="BUG", confidence=0.5, rationale="Crash report.")
    assert result.category == "bug"


def test_classify_result_rejects_unknown_category() -> None:
    with pytest.raises(ValidationError):
        ClassifyResult(category="urgent", confidence=0.5, rationale="Unknown.")


def test_summarise_result_rejects_negative_word_count() -> None:
    with pytest.raises(ValidationError):
        SummariseResult(summary="text", word_count=-1)
