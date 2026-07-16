"""Route agent actions to the correct specialist tool."""

from __future__ import annotations

from app.services.llm_service import LLMService
from app.services.tools import doc_summariser, story_estimator, tech_stack_advisor


class ToolDispatchError(ValueError):
    """Raised when an action cannot be dispatched."""


# dispatch_tool - execute the named tool and return its observation string
def dispatch_tool(
    action: str,
    action_input: str,
    *,
    service: LLMService | None = None,
) -> str:
    """Execute the named tool and return its observation string."""
    if action == "story_estimator":
        return story_estimator(action_input, service=service)
    if action == "tech_stack_advisor":
        return tech_stack_advisor(action_input, service=service)
    if action == "doc_summariser":
        return doc_summariser(action_input, service=service)
    raise ToolDispatchError(f"Unknown action '{action}'.")
