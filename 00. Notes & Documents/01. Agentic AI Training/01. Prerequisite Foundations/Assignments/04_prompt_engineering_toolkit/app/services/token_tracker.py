"""Token usage tracking for LLM calls."""

from __future__ import annotations

from typing import Any


class TokenTracker:
    """Accumulates prompt and completion token counts across calls."""

    def __init__(self) -> None:
        self.prompt_tokens = 0
        self.completion_tokens = 0

    def reset(self) -> None:
        self.prompt_tokens = 0
        self.completion_tokens = 0

    def record(self, usage: Any) -> None:
        self.prompt_tokens += getattr(usage, "prompt_tokens", 0) or 0
        self.completion_tokens += getattr(usage, "completion_tokens", 0) or 0

    @property
    def running_total(self) -> int:
        return self.prompt_tokens + self.completion_tokens

    def format_last_call(self, usage: Any) -> str:
        prompt = getattr(usage, "prompt_tokens", 0) or 0
        completion = getattr(usage, "completion_tokens", 0) or 0
        return (
            f"  tokens: prompt={prompt}, completion={completion}, "
            f"running_total={self.running_total}"
        )
