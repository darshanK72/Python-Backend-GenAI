"""Transcript formatting helpers."""

from __future__ import annotations

from autogen_agentchat.base import TaskResult
from autogen_agentchat.messages import BaseChatMessage


# format_transcript - flatten AutoGen chat messages into a readable transcript
def format_transcript(result: TaskResult | list[BaseChatMessage]) -> str:
    """Flatten AutoGen chat messages into a readable transcript."""
    messages = result.messages if isinstance(result, TaskResult) else result
    lines: list[str] = []
    for message in messages:
        source = getattr(message, "source", "unknown")
        content = getattr(message, "content", "")
        if isinstance(content, list):
            content = " ".join(str(item) for item in content)
        lines.append(f"{source}: {str(content).strip()}")
    return "\n\n".join(line for line in lines if line.strip())
