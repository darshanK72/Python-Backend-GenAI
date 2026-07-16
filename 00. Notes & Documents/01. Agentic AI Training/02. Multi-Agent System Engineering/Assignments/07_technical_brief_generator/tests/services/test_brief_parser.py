"""Tests for brief output parsing."""

from app.services.brief_parser import merge_facts, parse_analyst_json, parse_numbered_facts


# test_parse_numbered_facts - test extracting numbered facts from researcher output
def test_parse_numbered_facts() -> None:
    text = "1. Kafka buffers events.\n2. Consumers read asynchronously.\n"
    assert len(parse_numbered_facts(text)) == 2


# test_merge_facts_skips_duplicates - test that merge_facts ignores case-insensitive duplicates
def test_merge_facts_skips_duplicates() -> None:
    merged = merge_facts(["Kafka buffers events."], ["kafka buffers events.", "New fact."])
    assert len(merged) == 2


# test_parse_analyst_json - test parsing analyst JSON with claim_count
def test_parse_analyst_json() -> None:
    payload = parse_analyst_json(
        '{"insights":["a"],"claims":["REST uses HTTP verbs.","GraphQL uses one endpoint."],'
        '"claim_count":2}'
    )
    assert payload["claim_count"] == 2
    assert len(payload["claims"]) == 2
