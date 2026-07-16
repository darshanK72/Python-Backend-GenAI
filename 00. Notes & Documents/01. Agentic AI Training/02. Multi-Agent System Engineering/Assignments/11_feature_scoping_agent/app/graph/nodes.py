"""Plan-and-execute graph nodes."""

from __future__ import annotations

import json

from app.cli.output import print_execution_step, print_plan, print_review
from app.config import EXECUTOR_TEMPERATURE, PLANNER_TEMPERATURE
from app.graph.state import ScopeState
from app.schemas.prompts import (
    EXECUTOR_SYSTEM,
    EXECUTOR_USER,
    PLANNER_RETRY_USER,
    PLANNER_SYSTEM,
    PLANNER_USER,
    REVIEWER_SYSTEM,
    REVIEWER_USER,
)
from app.services.llm_service import LLMService
from app.services.scope_parser import (
    format_step_result,
    parse_executor_json,
    parse_plan_json,
    parse_review_json,
)


# make_planner_node - create the planner node that returns a 4–6 step JSON plan
def make_planner_node(service: LLMService):
    """Create the planner node that returns a 4–6 step JSON plan."""

    def planner_node(state: ScopeState) -> ScopeState:
        raw = service.chat(
            [
                {"role": "system", "content": PLANNER_SYSTEM},
                {"role": "user", "content": PLANNER_USER.format(request=state["request"])},
            ],
            temperature=PLANNER_TEMPERATURE,
        )
        try:
            plan = parse_plan_json(raw)
        except (ValueError, TypeError, json.JSONDecodeError):
            raw = service.chat(
                [
                    {"role": "system", "content": PLANNER_SYSTEM},
                    {
                        "role": "user",
                        "content": PLANNER_RETRY_USER.format(
                            request=state["request"],
                            bad_response=raw,
                        ),
                    },
                ],
                temperature=PLANNER_TEMPERATURE,
            )
            plan = parse_plan_json(raw)

        print_plan(plan)
        return ScopeState(
            request=state["request"],
            plan=plan,
            current_step_idx=0,
            execution_log=[],
            review=state["review"],
        )

    return planner_node


# make_executor_node - create the executor node that scopes one plan step per iteration
def make_executor_node(service: LLMService):
    """Create the executor node that scopes one plan step per iteration."""

    def executor_node(state: ScopeState) -> ScopeState:
        step_idx = state["current_step_idx"]
        step = state["plan"][step_idx]
        total = len(state["plan"])
        prior_log = "\n".join(state["execution_log"]) or "None"

        raw = service.chat(
            [
                {"role": "system", "content": EXECUTOR_SYSTEM},
                {
                    "role": "user",
                    "content": EXECUTOR_USER.format(
                        request=state["request"],
                        step_number=step_idx + 1,
                        total_steps=total,
                        step_name=step["step_name"],
                        description=step["description"],
                        expected_output=step["expected_output"],
                        acceptance_criteria=step["acceptance_criteria"],
                        prior_log=prior_log,
                    ),
                },
            ],
            temperature=EXECUTOR_TEMPERATURE,
        )
        execution = parse_executor_json(raw)
        entry = f"Step {step_idx + 1}/{total}: {format_step_result(execution)}"
        log = list(state["execution_log"])
        log.append(entry)
        print_execution_step(entry)

        return ScopeState(
            request=state["request"],
            plan=state["plan"],
            current_step_idx=step_idx + 1,
            execution_log=log,
            review=state["review"],
        )

    return executor_node


# make_reviewer_node - create the reviewer node that scores delivery readiness
def make_reviewer_node(service: LLMService):
    """Create the reviewer node that scores delivery readiness."""

    def reviewer_node(state: ScopeState) -> ScopeState:
        raw = service.chat(
            [
                {"role": "system", "content": REVIEWER_SYSTEM},
                {
                    "role": "user",
                    "content": REVIEWER_USER.format(
                        request=state["request"],
                        execution_log="\n".join(state["execution_log"]),
                    ),
                },
            ],
            temperature=0.0,
        )
        review = parse_review_json(raw)
        print_review(review)
        return ScopeState(
            request=state["request"],
            plan=state["plan"],
            current_step_idx=state["current_step_idx"],
            execution_log=state["execution_log"],
            review=review,
        )

    return reviewer_node
