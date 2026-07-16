"""Token usage tracking for LLM calls."""

from __future__ import annotations

from typing import Any


class TokenTracker:
    """Accumulates prompt and completion token counts across calls."""

    # __init__ - initialise token counters to zero
    def __init__(self) -> None:
        self.prompt_tokens = 0
        self.completion_tokens = 0

    # reset - clear accumulated token counts
    def reset(self) -> None:
        self.prompt_tokens = 0
        self.completion_tokens = 0

    # record - add usage from one LLM response
    def record(self, usage: Any) -> None:
        self.prompt_tokens += getattr(usage, "prompt_tokens", 0) or 0
        self.completion_tokens += getattr(usage, "completion_tokens", 0) or 0

    # running_total - return total prompt plus completion tokens recorded so far
    @property
    def running_total(self) -> int:
        return self.prompt_tokens + self.completion_tokens

    # format_last_call - format token usage for the most recent LLM call
    def format_last_call(self, usage: Any) -> str:
        prompt = getattr(usage, "prompt_tokens", 0) or 0
        completion = getattr(usage, "completion_tokens", 0) or 0
        return (
            f"  tokens: prompt={prompt}, completion={completion}, "
            f"running_total={self.running_total}"
        )
