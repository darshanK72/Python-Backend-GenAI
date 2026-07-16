"""Integration tests for the scoping graph."""

from __future__ import annotations

from unittest.mock import MagicMock

from app.graph.builder import build_graph
from app.graph.state import initial_state
from app.services.llm_service import LLMService

# SAMPLE_PLAN - valid 4-step planner JSON used across graph tests
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

# EXECUTOR_RESPONSE - valid executor JSON for one step
EXECUTOR_RESPONSE = """{
  "technical_approach": "Subscribe to task status change events and send templated email.",
  "dependencies": "Task service event bus",
  "effort_estimate": "small"
}"""

# REVIEW_RESPONSE - valid reviewer JSON after all steps complete
REVIEW_RESPONSE = """{
  "coverage_score": 4,
  "gaps": ["Retry policy for failed emails"],
  "recommendation": "Approved for development"
}"""


# test_graph_executes_all_steps_before_review - test executor loop then reviewer
def test_graph_executes_all_steps_before_review(test_settings) -> None:
    client = MagicMock()
    client.chat.completions.create.side_effect = [
        _response(SAMPLE_PLAN),
        _response(EXECUTOR_RESPONSE),
        _response(EXECUTOR_RESPONSE),
        _response(EXECUTOR_RESPONSE),
        _response(EXECUTOR_RESPONSE),
        _response(REVIEW_RESPONSE),
    ]
    service = LLMService(settings=test_settings, client=client)
    result = build_graph(service).invoke(
        initial_state("Add email notifications when a task's status changes to blocked")
    )

    assert len(result["plan"]) == 4
    assert len(result["execution_log"]) == 4
    assert result["current_step_idx"] == 4
    assert result["execution_log"][0].startswith("Step 1/4:")
    assert result["execution_log"][-1].startswith("Step 4/4:")
    assert result["review"]["coverage_score"] == 4
    assert result["review"]["recommendation"] == "Approved for development"


# test_planner_retries_on_invalid_json - test one planner correction retry on bad JSON
def test_planner_retries_on_invalid_json(test_settings) -> None:
    client = MagicMock()
    client.chat.completions.create.side_effect = [
        _response("not json"),
        _response(SAMPLE_PLAN),
        _response(EXECUTOR_RESPONSE),
        _response(EXECUTOR_RESPONSE),
        _response(EXECUTOR_RESPONSE),
        _response(EXECUTOR_RESPONSE),
        _response(REVIEW_RESPONSE),
    ]
    service = LLMService(settings=test_settings, client=client)
    result = build_graph(service).invoke(initial_state("Feature A"))
    assert len(result["plan"]) == 4


# _response - build a mocked chat completion response
def _response(content: str) -> MagicMock:
    return MagicMock(
        choices=[MagicMock(message=MagicMock(content=content))]
    )
