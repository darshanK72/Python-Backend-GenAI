"""Tests for JSON parsing helpers."""

import pytest

from app.services.scope_parser import parse_executor_json, parse_plan_json, parse_review_json

# SAMPLE_PLAN - valid 4-step planner JSON for parser tests
SAMPLE_PLAN = """[
  {
    "step_name": "Requirements",
    "description": "Capture notification rules",
    "expected_output": "Requirements doc",
    "acceptance_criteria": "Stakeholders sign off"
  },
  {
    "step_name": "Design",
    "description": "Design email flow",
    "expected_output": "Sequence diagram",
    "acceptance_criteria": "Covers blocked status trigger"
  },
  {
    "step_name": "Implementation",
    "description": "Build notifier service",
    "expected_output": "Working email trigger",
    "acceptance_criteria": "Email sent on blocked status"
  },
  {
    "step_name": "Testing",
    "description": "Validate notifications",
    "expected_output": "Test report",
    "acceptance_criteria": "All scenarios pass"
  }
]"""


# test_parse_plan_json_accepts_valid_plan - test that a valid plan parses to four steps
def test_parse_plan_json_accepts_valid_plan() -> None:
    plan = parse_plan_json(SAMPLE_PLAN)
    assert len(plan) == 4
    assert plan[0]["step_name"] == "Requirements"


# test_parse_plan_json_rejects_too_few_steps - test that empty plans are rejected
def test_parse_plan_json_rejects_too_few_steps() -> None:
    with pytest.raises(ValueError, match="4-6 steps"):
        parse_plan_json("[]")


# test_parse_executor_json - test that executor JSON normalises effort_estimate
def test_parse_executor_json() -> None:
    payload = """{
      "technical_approach": "Listen to task status events.",
      "dependencies": "Task service and SMTP provider",
      "effort_estimate": "medium"
    }"""
    result = parse_executor_json(payload)
    assert result["effort_estimate"] == "medium"


# test_parse_review_json - test that reviewer JSON returns score and gaps
def test_parse_review_json() -> None:
    payload = """{
      "coverage_score": 4,
      "gaps": ["Disaster recovery"],
      "recommendation": "Approved for development"
    }"""
    review = parse_review_json(payload)
    assert review["coverage_score"] == 4
    assert review["gaps"] == ["Disaster recovery"]
