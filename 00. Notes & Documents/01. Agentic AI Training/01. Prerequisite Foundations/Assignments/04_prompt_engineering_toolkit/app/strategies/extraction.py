"""Prompting strategy entry points."""

from __future__ import annotations

import json
from typing import Any

from app.schemas.extraction import CORRECTIVE_JSON_INSTRUCTION, FEWSHOT_EXAMPLES, SYSTEM_PROMPT
from app.services.llm_service import LLMService


# build_naive_messages - build the minimal one-line naive prompt
def build_naive_messages(report: str) -> list[dict[str, str]]:
    """Build the minimal one-line naive prompt."""
    return [
        {
            "role": "user",
            "content": f"Extract summary, component, severity, and reproducible from: {report}",
        },
    ]


# build_structured_messages - build role plus schema structured prompt messages
def build_structured_messages(report: str) -> list[dict[str, str]]:
    """Build role + schema structured prompt messages."""
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"Bug report:\n{report}"},
    ]


# build_fewshot_messages - build few-shot prompt with worked examples before the target report
def build_fewshot_messages(report: str) -> list[dict[str, str]]:
    """Build few-shot prompt with worked examples before the target report."""
    messages: list[dict[str, str]] = [{"role": "system", "content": SYSTEM_PROMPT}]
    for index, (example_input, example_output) in enumerate(FEWSHOT_EXAMPLES, start=1):
        messages.append(
            {
                "role": "user",
                "content": (
                    f"Example {index} input: {example_input}\n"
                    f"Example {index} output: {json.dumps(example_output, separators=(',', ':'))}"
                ),
            },
        )
    messages.append({"role": "user", "content": f"Bug report:\n{report}"})
    return messages


# naive_extract - extract bug fields with a minimal one-line prompt
def naive_extract(report: str, *, service: LLMService | None = None) -> str:
    """Extract bug fields with a minimal one-line prompt."""
    llm = service or LLMService()
    return llm.chat(build_naive_messages(report))


# structured_extract - extract bug fields using role, explicit schema, and JSON-only instructions
def structured_extract(report: str, *, service: LLMService | None = None) -> dict[str, Any]:
    """Extract bug fields using role, explicit schema, and JSON-only instructions."""
    llm = service or LLMService()
    messages = build_structured_messages(report)
    raw = llm.chat(messages)
    return llm.parse_structured(
        raw,
        messages,
        corrective_instruction=CORRECTIVE_JSON_INSTRUCTION,
    )


# fewshot_extract - extract bug fields using structured prompting plus worked examples
def fewshot_extract(report: str, *, service: LLMService | None = None) -> dict[str, Any]:
    """Extract bug fields using structured prompting plus worked examples."""
    llm = service or LLMService()
    messages = build_fewshot_messages(report)
    raw = llm.chat(messages)
    return llm.parse_structured(
        raw,
        messages,
        corrective_instruction=CORRECTIVE_JSON_INSTRUCTION,
    )
