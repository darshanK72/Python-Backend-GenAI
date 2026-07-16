"""Delivery report generation and validation."""

from __future__ import annotations

from autogen_agentchat.base import TaskResult
from autogen_ext.models.openai import OpenAIChatCompletionClient

from app.agents.definitions import create_documentation_writer
from app.config import REPORT_SECTIONS


# generate_delivery_report - ask DocumentationWriter to produce delivery_report.md
async def generate_delivery_report(
    transcript: str,
    model_client: OpenAIChatCompletionClient,
) -> str:
    """Ask DocumentationWriter to produce delivery_report.md from the transcript."""
    writer = create_documentation_writer(model_client)
    prompt = (
        "Write delivery_report.md from this group chat transcript.\n\n"
        f"Transcript:\n{transcript}"
    )
    result: TaskResult = await writer.run(task=prompt)
    if result.messages:
        content = result.messages[-1].content
        if isinstance(content, list):
            return "\n".join(str(item) for item in content)
        return str(content).strip()
    return ""


# validate_report_sections - return missing required report section headings
def validate_report_sections(report: str) -> list[str]:
    """Return missing required report section headings."""
    return [section for section in REPORT_SECTIONS if section not in report]
