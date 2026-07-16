"""Tests for quality gate routing."""

from app.config import MAX_RETRIES, MIN_CLAIMS
from app.graph.builder import route_after_analyst
from app.graph.state import initial_state


# test_route_to_writer_when_enough_claims - test gate passes when claim_count >= MIN_CLAIMS
def test_route_to_writer_when_enough_claims() -> None:
    state = initial_state("topic")
    state["claim_count"] = MIN_CLAIMS
    assert route_after_analyst(state) == "writer"


# test_route_to_researcher_when_claims_low_and_retries_remain - test gate retries researcher
def test_route_to_researcher_when_claims_low_and_retries_remain() -> None:
    state = initial_state("topic")
    state["claim_count"] = MIN_CLAIMS - 1
    state["retry_count"] = 0
    assert route_after_analyst(state) == "researcher"


# test_route_to_writer_when_retry_limit_reached - test gate forwards to writer after max retries
def test_route_to_writer_when_retry_limit_reached() -> None:
    state = initial_state("topic")
    state["claim_count"] = 2
    state["retry_count"] = MAX_RETRIES
    assert route_after_analyst(state) == "writer"
