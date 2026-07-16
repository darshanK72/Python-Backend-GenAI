"""Feature scoping graph state."""

from __future__ import annotations

from typing import TypedDict


class PlanStep(TypedDict):
    """One planner delivery step."""

    step_name: str
    description: str
    expected_output: str
    acceptance_criteria: str


class StepExecution(TypedDict):
    """Executor output for a single plan step."""

    technical_approach: str
    dependencies: str
    effort_estimate: str


class ReviewResult(TypedDict):
    """Reviewer delivery-readiness assessment."""

    coverage_score: int
    gaps: list[str]
    recommendation: str


class ScopeState(TypedDict):
    """LangGraph state for the plan-and-execute scoping flow."""

    request: str
    plan: list[PlanStep]
    current_step_idx: int
    execution_log: list[str]
    review: ReviewResult


# initial_state - build the starting ScopeState for a feature request
def initial_state(request: str) -> ScopeState:
    """Build the starting ScopeState for a feature request."""
    empty_review = ReviewResult(coverage_score=0, gaps=[], recommendation="")
    return ScopeState(
        request=request,
        plan=[],
        current_step_idx=0,
        execution_log=[],
        review=empty_review,
    )
