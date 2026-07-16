"""Extract a SQL statement from an LLM response."""

from __future__ import annotations

import re


# extract_sql - pull a SELECT statement from fenced or plain LLM text
def extract_sql(text: str) -> str:
    """Pull a SELECT statement from fenced or plain LLM text."""
    fenced = re.search(r"```(?:sql)?\s*(.*?)```", text, flags=re.IGNORECASE | re.DOTALL)
    if fenced:
        return fenced.group(1).strip().rstrip(";")
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    for line in lines:
        if line.upper().startswith("SELECT"):
            return line.rstrip(";")
    return text.strip().rstrip(";")
