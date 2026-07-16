"""Tests for Pydantic LLM schemas."""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from app.schemas.llm import ClassifyResult, SummariseResult


# test_classify_result_normalises_category - test that ClassifyResult normalises category to lowercase
def test_classify_result_normalises_category() -> None:
    result = ClassifyResult(category="BUG", confidence=0.5, rationale="Crash report.")
    assert result.category == "bug"


# test_classify_result_rejects_unknown_category - test that ClassifyResult rejects unknown categories
def test_classify_result_rejects_unknown_category() -> None:
    with pytest.raises(ValidationError):
        ClassifyResult(category="urgent", confidence=0.5, rationale="Unknown.")


# test_summarise_result_rejects_negative_word_count - test that SummariseResult rejects negative word counts
def test_summarise_result_rejects_negative_word_count() -> None:
    with pytest.raises(ValidationError):
        SummariseResult(summary="text", word_count=-1)
