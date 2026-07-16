"""Supervisor routing helpers."""

from __future__ import annotations

import re

from app.schemas.prompts import SUPERVISOR_SYSTEM, SUPERVISOR_USER
from app.services.llm_service import LLMService

# VALID_ROUTES - worker names and FINISH accepted by the supervisor
VALID_ROUTES = {
    "sprint_builder",
    "capacity_checker",
    "risk_assessor",
    "FINISH",
}


# route_by_keywords - match common request phrases to a worker route
def route_by_keywords(request: str) -> str | None:
    """Match common request phrases to a worker route."""
    text = request.lower()
    if any(word in text for word in ("done", "that's all", "nothing else", "quit")):
        return "FINISH"
    if any(word in text for word in ("plan", "add tasks", "break down")):
        return "sprint_builder"
    if any(word in text for word in ("capacity", "how many sp", "over budget", "velocity")):
        return "capacity_checker"
    if any(word in text for word in ("risk", "go wrong", "blockers", "concerns")):
        return "risk_assessor"
    return None


# classify_request - route by keywords first, then fall back to LLM classification
def classify_request(request: str, *, service: LLMService | None = None) -> str:
    """Route by keywords first, then fall back to LLM classification."""
    keyword_route = route_by_keywords(request)
    if keyword_route is not None:
        return keyword_route

    llm = service or LLMService()
    raw = llm.chat(
        [
            {"role": "system", "content": SUPERVISOR_SYSTEM},
            {"role": "user", "content": SUPERVISOR_USER.format(request=request)},
        ],
        temperature=0.0,
    )
    match = re.search(
        r"\b(sprint_builder|capacity_checker|risk_assessor|FINISH)\b",
        raw,
        flags=re.IGNORECASE,
    )
    if match:
        route = match.group(1).lower()
        return "FINISH" if route == "finish" else route
    return "sprint_builder"
