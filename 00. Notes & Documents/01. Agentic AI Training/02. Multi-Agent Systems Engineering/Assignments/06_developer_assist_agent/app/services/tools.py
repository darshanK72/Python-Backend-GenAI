"""Developer assist specialist tools."""

from __future__ import annotations

import re

from app.schemas.prompts import (
    DOC_SUMMARISER_PROMPT,
    STORY_ESTIMATOR_PROMPT,
    TECH_STACK_ADVISOR_PROMPT,
)
from app.services.llm_service import LLMService

VALID_STORY_POINTS = {1, 2, 3, 5, 8, 13}


def story_estimator(description: str, *, service: LLMService | None = None) -> str:
    """Return a story point estimate with a two-sentence rationale."""
    llm = service or LLMService()
    result = llm.chat(
        [
            {
                "role": "system",
                "content": "You estimate agile story points for software features.",
            },
            {"role": "user", "content": STORY_ESTIMATOR_PROMPT + description},
        ],
        temperature=0.2,
    ).strip()
    if not _contains_story_point(result):
        raise ValueError("story_estimator must return one of 1, 2, 3, 5, 8, or 13.")
    return result


def tech_stack_advisor(requirements: str, *, service: LLMService | None = None) -> str:
    """Return two or three stack recommendations with reasons."""
    llm = service or LLMService()
    result = llm.chat(
        [
            {
                "role": "system",
                "content": "You recommend practical engineering tools and frameworks.",
            },
            {"role": "user", "content": TECH_STACK_ADVISOR_PROMPT + requirements},
        ],
        temperature=0.2,
    ).strip()
    lines = [line.strip(" -") for line in result.splitlines() if line.strip()]
    if not 2 <= len(lines) <= 3:
        raise ValueError("tech_stack_advisor must return 2-3 recommendations.")
    return "\n".join(lines)


def doc_summariser(text: str, *, service: LLMService | None = None) -> str:
    """Return exactly three one-sentence bullet points."""
    llm = service or LLMService()
    result = llm.chat(
        [
            {
                "role": "system",
                "content": "You summarise technical documentation concisely.",
            },
            {"role": "user", "content": DOC_SUMMARISER_PROMPT + text},
        ],
        temperature=0.2,
    ).strip()
    bullets = [line.strip() for line in result.splitlines() if line.strip().startswith("-")]
    if len(bullets) != 3:
        raise ValueError("doc_summariser must return exactly 3 bullet points.")
    return "\n".join(bullets)


def _contains_story_point(text: str) -> bool:
    return any(str(points) in text for points in VALID_STORY_POINTS) or bool(
        re.search(r"\b(1|2|3|5|8|13)\s*points?\b", text, flags=re.IGNORECASE)
    )
