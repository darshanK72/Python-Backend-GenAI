"""JSON parsing helpers for LLM structured output."""

from __future__ import annotations

import json
import re
from typing import Any


class LLMJsonParseError(ValueError):
    """Raised when structured JSON cannot be parsed after retry."""


# extract_json_block - parse JSON from raw model text, stripping optional markdown fences
def extract_json_block(text: str) -> dict[str, Any]:
    """Parse JSON from raw model text, stripping optional markdown fences."""
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned)
        cleaned = re.sub(r"\s*```$", "", cleaned)
    data = json.loads(cleaned)
    if not isinstance(data, dict):
        raise json.JSONDecodeError("Expected JSON object", cleaned, 0)
    return data
