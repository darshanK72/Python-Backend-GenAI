"""Supervisor routing helpers."""

from __future__ import annotations

import re

from app.schemas.prompts import SUPERVISOR_SYSTEM, SUPERVISOR_USER
from app.services.llm_service import LLMService

# VALID_ROUTES - allowed supervisor routing tokens
VALID_ROUTES = {"rag", "db", "memory", "FINISH"}


# route_by_keywords - fast keyword heuristic before LLM fallback
def route_by_keywords(query: str) -> str | None:
    text = query.lower()
    if any(word in text for word in ("done", "thanks", "that's all", "thank you")):
        return "FINISH"
    if any(
        phrase in text
        for phrase in (
            "what have i asked",
            "recap",
            "our conversation",
            "so far",
            "what did i ask",
        )
    ):
        return "memory"
    if any(
        word in text
        for word in (
            "task",
            "blocked",
            "incident",
            "team member",
            "story point",
            "assignee",
            "sprint",
            "project",
        )
    ) and not any(word in text for word in ("best practice", "devops", "microservices")):
        return "db"
    if any(
        word in text
        for word in (
            "what is",
            "how do",
            "microservices",
            "monolith",
            "trunk-based",
            "methodology",
            "best practice",
            "devops",
            "architecture",
        )
    ):
        return "rag"
    return None


# is_ambiguous - detect Query-4 style session + DB + methodology hybrids
def is_ambiguous(query: str) -> bool:
    text = query.lower()
    has_session = any(word in text for word in ("conversation", "our", "based on"))
    has_db = any(word in text for word in ("blocked", "task", "incident"))
    has_rag = any(word in text for word in ("best practice", "devops", "methodology"))
    return has_session and has_db and has_rag


# classify_query - choose rag | db | memory | FINISH for a query
def classify_query(
    query: str,
    session_context: str = "",
    *,
    service: LLMService | None = None,
) -> str:
    if is_ambiguous(query):
        return "rag"

    keyword_route = route_by_keywords(query)
    if keyword_route is not None:
        return keyword_route

    llm = service or LLMService()
    raw = llm.chat(
        [
            {"role": "system", "content": SUPERVISOR_SYSTEM},
            {
                "role": "user",
                "content": SUPERVISOR_USER.format(
                    query=query,
                    session_context=session_context or "None",
                ),
            },
        ],
        temperature=0.0,
    )
    match = re.search(r"\b(rag|db|memory|finish)\b", raw, flags=re.IGNORECASE)
    if match:
        route = match.group(1).lower()
        return "FINISH" if route == "finish" else route
    return "rag"
