"""Preflight token counting with tiktoken (before calling the API)."""

from __future__ import annotations

import tiktoken


def count_text_tokens(text: str, model: str) -> tuple[int, str]:
    try:
        encoding = tiktoken.encoding_for_model(model)
        encoding_name = encoding.name
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")
        encoding_name = "cl100k_base"
    return len(encoding.encode(text)), encoding_name
