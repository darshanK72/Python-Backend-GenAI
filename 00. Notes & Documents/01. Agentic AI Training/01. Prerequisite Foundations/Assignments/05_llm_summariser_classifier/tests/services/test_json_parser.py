"""Tests for JSON parsing helpers."""

from __future__ import annotations

import json

import pytest

from app.services.json_parser import extract_json_block


# test_extract_json_block_parses_plain_object - test that extract_json_block parses a plain JSON object
def test_extract_json_block_parses_plain_object() -> None:
    result = extract_json_block('{"summary":"x","word_count":3}')
    assert result["summary"] == "x"
    assert result["word_count"] == 3


# test_extract_json_block_strips_markdown_fence - test that extract_json_block strips markdown code fences
def test_extract_json_block_strips_markdown_fence() -> None:
    raw = '```json\n{"category":"bug","confidence":0.9,"rationale":"crash"}\n```'
    result = extract_json_block(raw)
    assert result["category"] == "bug"


# test_extract_json_block_rejects_non_object - test that extract_json_block rejects non-object JSON
def test_extract_json_block_rejects_non_object() -> None:
    with pytest.raises(json.JSONDecodeError):
        extract_json_block("[1, 2]")
