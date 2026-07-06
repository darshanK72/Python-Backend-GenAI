"""Tests for JSON parsing helpers."""

from __future__ import annotations

import json

import pytest

from app.services.json_parser import extract_json_block


def test_extract_json_block_parses_plain_object() -> None:
    result = extract_json_block('{"summary":"x","component":"y","severity":"low","reproducible":false}')

    assert result["summary"] == "x"
    assert result["severity"] == "low"
    assert result["reproducible"] is False


def test_extract_json_block_strips_markdown_fence() -> None:
    raw = '```json\n{"summary":"x","component":"y","severity":"high","reproducible":true}\n```'
    result = extract_json_block(raw)

    assert result["severity"] == "high"


def test_extract_json_block_rejects_non_object() -> None:
    with pytest.raises(json.JSONDecodeError):
        extract_json_block("[1, 2, 3]")
