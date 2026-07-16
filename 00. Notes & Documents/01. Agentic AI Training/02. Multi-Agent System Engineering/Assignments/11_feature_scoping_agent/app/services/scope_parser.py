"""Parse planner, executor, and reviewer JSON outputs."""

from __future__ import annotations

import json
import re

from app.config import MAX_PLAN_STEPS, MIN_PLAN_STEPS
from app.graph.state import PlanStep, ReviewResult, StepExecution

# REQUIRED_STEP_FIELDS - fields every planner step object must include
REQUIRED_STEP_FIELDS = (
    "step_name",
    "description",
    "expected_output",
    "acceptance_criteria",
)


# extract_json_block - pull a JSON object or array from LLM text
def extract_json_block(text: str) -> str:
    """Pull a JSON object or array from LLM text (fenced or raw)."""
    fenced = re.search(r"```(?:json)?\s*(.*?)```", text, flags=re.IGNORECASE | re.DOTALL)
    if fenced:
        return fenced.group(1).strip()

    obj_start = text.find("{")
    arr_start = text.find("[")
    if obj_start != -1 and (arr_start == -1 or obj_start < arr_start):
        obj_end = text.rfind("}")
        if obj_end != -1 and obj_end > obj_start:
            return text[obj_start : obj_end + 1]

    if arr_start != -1:
        arr_end = text.rfind("]")
        if arr_end != -1 and arr_end > arr_start:
            return text[arr_start : arr_end + 1]

    return text.strip()


# parse_plan_json - validate and normalise a 4–6 step planner JSON array
def parse_plan_json(text: str) -> list[PlanStep]:
    """Validate and normalise a 4–6 step planner JSON array."""
    payload = json.loads(extract_json_block(text))
    if not isinstance(payload, list):
        raise ValueError("Plan must be a JSON array")
    steps: list[PlanStep] = []
    for item in payload:
        if not isinstance(item, dict):
            raise ValueError("Each plan step must be a JSON object")
        missing = [field for field in REQUIRED_STEP_FIELDS if field not in item]
        if missing:
            raise ValueError(f"Plan step missing fields: {', '.join(missing)}")
        steps.append(
            PlanStep(
                step_name=str(item["step_name"]).strip(),
                description=str(item["description"]).strip(),
                expected_output=str(item["expected_output"]).strip(),
                acceptance_criteria=str(item["acceptance_criteria"]).strip(),
            )
        )
    if not MIN_PLAN_STEPS <= len(steps) <= MAX_PLAN_STEPS:
        raise ValueError(
            f"Plan must contain {MIN_PLAN_STEPS}-{MAX_PLAN_STEPS} steps, got {len(steps)}"
        )
    return steps


# parse_executor_json - validate executor technical approach JSON
def parse_executor_json(text: str) -> StepExecution:
    """Validate executor technical approach JSON."""
    payload = json.loads(extract_json_block(text))
    if not isinstance(payload, dict):
        raise ValueError("Executor output must be a JSON object")
    for field in ("technical_approach", "dependencies", "effort_estimate"):
        if field not in payload:
            raise ValueError(f"Executor output missing field: {field}")
    effort = str(payload["effort_estimate"]).strip().lower()
    if effort not in {"small", "medium", "large"}:
        raise ValueError("effort_estimate must be small, medium, or large")
    return StepExecution(
        technical_approach=str(payload["technical_approach"]).strip(),
        dependencies=str(payload["dependencies"]).strip(),
        effort_estimate=effort,
    )


# format_step_result - flatten executor JSON into an execution_log string
def format_step_result(execution: StepExecution) -> str:
    """Flatten executor JSON into an execution_log string."""
    return (
        f"Technical approach: {execution['technical_approach']} "
        f"Dependencies: {execution['dependencies']} "
        f"Effort: {execution['effort_estimate']}"
    )


# parse_review_json - validate reviewer coverage / gaps / recommendation JSON
def parse_review_json(text: str) -> ReviewResult:
    """Validate reviewer coverage / gaps / recommendation JSON."""
    payload = json.loads(extract_json_block(text))
    if not isinstance(payload, dict):
        raise ValueError("Review output must be a JSON object")
    for field in ("coverage_score", "gaps", "recommendation"):
        if field not in payload:
            raise ValueError(f"Review output missing field: {field}")
    score = int(payload["coverage_score"])
    if score < 1 or score > 5:
        raise ValueError("coverage_score must be between 1 and 5")
    gaps = payload["gaps"]
    if not isinstance(gaps, list):
        raise ValueError("gaps must be a JSON array")
    return ReviewResult(
        coverage_score=score,
        gaps=[str(item).strip() for item in gaps],
        recommendation=str(payload["recommendation"]).strip(),
    )
