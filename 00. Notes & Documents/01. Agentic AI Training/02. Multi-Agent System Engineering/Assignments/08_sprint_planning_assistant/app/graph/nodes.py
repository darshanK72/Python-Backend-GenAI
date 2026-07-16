"""Supervisor and worker nodes."""

from __future__ import annotations

import re

from app.cli.output import (
    print_capacity_result,
    print_finish,
    print_request,
    print_risk_header,
    print_risk_result,
    print_sprint_builder_header,
    print_sprint_builder_tasks,
    print_supervisor_route,
)
from app.config import DEFAULT_VELOCITY
from app.graph.state import SprintState
from app.schemas.prompts import (
    RISK_ASSESSOR_SYSTEM,
    RISK_ASSESSOR_USER,
    SPRINT_BUILDER_SYSTEM,
    SPRINT_BUILDER_USER,
)
from app.services.llm_service import LLMService
from app.services.mcp_client import MCPClientWrapper
from app.services.router import classify_request
from app.services.task_parser import parse_task_plan


# make_supervisor_node - create the supervisor node that routes each request
def make_supervisor_node(service: LLMService):
    """Create the supervisor node that routes each request."""

    def supervisor_node(state: SprintState) -> SprintState:
        if state["finished"] or state["request_index"] >= len(state["requests"]):
            return SprintState(
                requests=state["requests"],
                request_index=state["request_index"],
                current_request=state["current_request"],
                route="FINISH",
                worker_result=state["worker_result"],
                results=state["results"],
                finished=True,
            )

        request = state["requests"][state["request_index"]]
        route = classify_request(request, service=service)
        print_request(request, index=state["request_index"])
        if route == "FINISH":
            print_finish()
        else:
            print_supervisor_route(route)

        finished = route == "FINISH"
        return SprintState(
            requests=state["requests"],
            request_index=state["request_index"],
            current_request=request,
            route=route,
            worker_result=state["worker_result"],
            results=state["results"],
            finished=finished,
        )

    return supervisor_node


# make_sprint_builder_node - create the sprint builder worker node
def make_sprint_builder_node(service: LLMService, mcp: MCPClientWrapper):
    """Create the sprint builder worker node."""

    def sprint_builder_node(state: SprintState) -> SprintState:
        raw = service.chat(
            [
                {"role": "system", "content": SPRINT_BUILDER_SYSTEM},
                {
                    "role": "user",
                    "content": SPRINT_BUILDER_USER.format(request=state["current_request"]),
                },
            ],
            temperature=0.2,
        )
        plan = parse_task_plan(raw)
        tasks = plan["tasks"]
        feature = plan.get("feature", state["current_request"])
        print_sprint_builder_header(feature)
        for task in tasks:
            mcp.call_tool(
                "add_task",
                {
                    "title": task["title"],
                    "assignee": task["assignee"],
                    "story_points": int(task["story_points"]),
                },
            )
        print_sprint_builder_tasks(tasks)
        result = f"Created {len(tasks)} tasks for {feature}"
        return _after_worker(state, result)

    return sprint_builder_node


# make_capacity_checker_node - create the capacity checker worker node
def make_capacity_checker_node(mcp: MCPClientWrapper):
    """Create the capacity checker worker node."""

    def capacity_checker_node(state: SprintState) -> SprintState:
        print("\n[capacity_checker]")
        capacity = mcp.call_tool("check_capacity", {"velocity": DEFAULT_VELOCITY})
        if "Over capacity" in capacity:
            backlog = mcp.call_tool("get_backlog", {})
            task_name = _largest_open_task(backlog)
            recommendation = f"Recommend descoping {task_name}"
        else:
            recommendation = "Sprint has room for additional items"
        print_capacity_result(capacity, recommendation, include_header=False)
        result = f"{capacity.rstrip('.')}. {recommendation}"
        return _after_worker(state, result)

    return capacity_checker_node


# make_risk_assessor_node - create the risk assessor worker node
def make_risk_assessor_node(service: LLMService, mcp: MCPClientWrapper):
    """Create the risk assessor worker node."""

    def risk_assessor_node(state: SprintState) -> SprintState:
        print_risk_header()
        backlog = mcp.call_tool("get_backlog", {})
        risks = mcp.call_tool("get_risk_summary", {})
        raw = service.chat(
            [
                {"role": "system", "content": RISK_ASSESSOR_SYSTEM},
                {
                    "role": "user",
                    "content": RISK_ASSESSOR_USER.format(
                        backlog=backlog,
                        risks=risks,
                        request=state["current_request"],
                    ),
                },
            ],
            temperature=0.2,
        )
        result = raw.strip()
        print_risk_result(result, include_header=False)
        return _after_worker(state, result)

    return risk_assessor_node


# _after_worker - advance request_index and append the worker result
def _after_worker(state: SprintState, result: str) -> SprintState:
    results = list(state["results"]) + [result]
    return SprintState(
        requests=state["requests"],
        request_index=state["request_index"] + 1,
        current_request=state["current_request"],
        route=state["route"],
        worker_result=result,
        results=results,
        finished=state["finished"],
    )


# _largest_open_task - find the highest-SP open task for descoping recommendations
def _largest_open_task(backlog_text: str) -> str:
    best_name = "DB migration"
    best_points = 0
    for line in backlog_text.splitlines():
        if "status=done" in line:
            continue
        match = re.search(r"^\d+\.\s+([^—]+)—\s+(\d+)\s+SP", line)
        if match:
            points = int(match.group(2))
            if points > best_points:
                best_points = points
                best_name = match.group(1).strip()
    return best_name
