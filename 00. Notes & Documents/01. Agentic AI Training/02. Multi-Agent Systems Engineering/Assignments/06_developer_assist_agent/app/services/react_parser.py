"""Parse structured ReAct responses from the LLM."""

from __future__ import annotations

import re
from dataclasses import dataclass

VALID_ACTIONS = {"story_estimator", "tech_stack_advisor", "doc_summariser"}


@dataclass(frozen=True)
class ReActDecision:
    """Parsed output from a single ReAct reasoning step."""

    thought: str
    action: str | None
    action_input: str
    final_answer: str


class ReActParseError(ValueError):
    """Raised when the model response does not match the ReAct format."""


def parse_react_response(text: str) -> ReActDecision:
    """Extract Thought plus either Action/Action Input or Final Answer."""
    normalized = text.strip()
    thought_match = re.search(
        r"^Thought:\s*(.+?)(?=^Action:|^Final Answer:|\Z)",
        normalized,
        flags=re.MULTILINE | re.DOTALL,
    )
    thought = thought_match.group(1).strip() if thought_match else ""

    final_match = re.search(r"^Final Answer:\s*(.+)$", normalized, flags=re.MULTILINE | re.DOTALL)
    if final_match:
        return ReActDecision(
            thought=thought,
            action=None,
            action_input="",
            final_answer=final_match.group(1).strip(),
        )

    action_match = re.search(r"^Action:\s*(\w+)\s*$", normalized, flags=re.MULTILINE)
    input_match = re.search(
        r"^Action Input:\s*(.+)$",
        normalized,
        flags=re.MULTILINE | re.DOTALL,
    )
    if not action_match or not input_match:
        raise ReActParseError("Response must include Action and Action Input or Final Answer.")

    action = action_match.group(1).strip()
    if action not in VALID_ACTIONS:
        raise ReActParseError(f"Unknown action '{action}'.")

    return ReActDecision(
        thought=thought,
        action=action,
        action_input=input_match.group(1).strip(),
        final_answer="",
    )
