"""Parse researcher and analyst LLM output."""

from __future__ import annotations

import json
import re


# parse_numbered_facts - extract numbered fact lines from researcher output
def parse_numbered_facts(text: str) -> list[str]:
    """Extract numbered fact lines from researcher output."""
    facts: list[str] = []
    for line in text.splitlines():
        cleaned = line.strip()
        if not cleaned:
            continue
        match = re.match(r"^\d+[\).\s]+(.+)$", cleaned)
        if match:
            facts.append(match.group(1).strip())
        elif cleaned.startswith("- "):
            facts.append(cleaned[2:].strip())
    return facts


# merge_facts - append only facts that are not already present
def merge_facts(existing: list[str], new_facts: list[str]) -> list[str]:
    """Append only facts that are not already present (case-insensitive)."""
    seen = {fact.lower() for fact in existing}
    merged = list(existing)
    for fact in new_facts:
        key = fact.lower()
        if key not in seen:
            merged.append(fact)
            seen.add(key)
    return merged


# parse_analyst_json - parse analyst JSON, including fenced code blocks
def parse_analyst_json(text: str) -> dict:
    """Parse analyst JSON, falling back to a fenced code block if present."""
    stripped = text.strip()
    if stripped.startswith("```"):
        stripped = stripped.strip("`")
        if stripped.startswith("json"):
            stripped = stripped[4:].strip()
    payload = json.loads(stripped)
    claims = payload.get("claims", [])
    payload["claim_count"] = int(payload.get("claim_count", len(claims)))
    payload["insights"] = list(payload.get("insights", []))
    payload["claims"] = list(claims)
    return payload
