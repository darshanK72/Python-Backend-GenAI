"""Tests for supervisor routing."""

from app.services.router import classify_request, route_by_keywords


# test_route_planning_keywords - test planning keywords route to sprint_builder
def test_route_planning_keywords() -> None:
    assert route_by_keywords("Plan OAuth login feature") == "sprint_builder"


# test_route_capacity_keywords - test capacity keywords route to capacity_checker
def test_route_capacity_keywords() -> None:
    assert route_by_keywords("Check capacity for this sprint") == "capacity_checker"


# test_route_risk_keywords - test risk keywords route to risk_assessor
def test_route_risk_keywords() -> None:
    assert route_by_keywords("Any risks we should worry about?") == "risk_assessor"


# test_route_finish_keywords - test finish keywords route to FINISH
def test_route_finish_keywords() -> None:
    assert route_by_keywords("Done") == "FINISH"


# test_classify_uses_keywords_without_llm - test keyword routing without LLM fallback
def test_classify_uses_keywords_without_llm() -> None:
    assert classify_request("Break down CSV export work") == "sprint_builder"
