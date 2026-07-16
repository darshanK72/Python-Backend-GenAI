"""Tests for supervisor graph routing."""

from app.graph.builder import route_after_supervisor, route_after_worker
from app.graph.state import initial_state


# test_route_after_supervisor_to_worker - test routing from supervisor to a worker
def test_route_after_supervisor_to_worker() -> None:
    state = initial_state(["Plan feature"])
    state["route"] = "sprint_builder"
    assert route_after_supervisor(state) == "sprint_builder"


# test_route_after_supervisor_to_end_on_finish - test routing to END on FINISH
def test_route_after_supervisor_to_end_on_finish() -> None:
    state = initial_state(["Done"])
    state["route"] = "FINISH"
    state["finished"] = True
    assert route_after_supervisor(state) == "end"


# test_route_after_worker_returns_supervisor - test worker loops back to supervisor
def test_route_after_worker_returns_supervisor() -> None:
    state = initial_state(["Plan feature", "Check capacity"])
    state["request_index"] = 1
    assert route_after_worker(state) == "supervisor"
