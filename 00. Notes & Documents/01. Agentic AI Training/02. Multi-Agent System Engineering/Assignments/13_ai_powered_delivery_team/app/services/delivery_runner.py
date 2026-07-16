"""End-to-end delivery team orchestration."""

from __future__ import annotations

import asyncio
from pathlib import Path

from app.agents.definitions import create_model_client
from app.agents.group_chat import run_group_chat
from app.config import FEATURE_REQUEST, REPORT_PATH, Settings, TRANSCRIPT_PATH, get_settings
from app.services.report_writer import generate_delivery_report, validate_report_sections
from app.services.transcript import format_transcript


# run_delivery_async - async orchestration: group chat → report → optional save
async def run_delivery_async(
    feature_request: str = FEATURE_REQUEST,
    *,
    settings: Settings | None = None,
    save_outputs: bool = False,
) -> tuple[str, str]:
    """Run group chat + documentation writer; optionally save artifacts."""
    cfg = settings or get_settings()
    if not cfg.openai_api_key:
        raise RuntimeError("OPENAI_API_KEY is not set in the environment.")

    model_client = create_model_client(cfg.openai_api_key, cfg.openai_model)
    chat_result = await run_group_chat(feature_request, model_client)
    transcript = format_transcript(chat_result)
    report = await generate_delivery_report(transcript, model_client)

    missing = validate_report_sections(report)
    if missing:
        raise RuntimeError(f"Delivery report missing sections: {', '.join(missing)}")

    if save_outputs:
        save_artifacts(transcript, report)

    return transcript, report


# run_delivery - synchronous wrapper around run_delivery_async
def run_delivery(
    feature_request: str = FEATURE_REQUEST,
    *,
    settings: Settings | None = None,
    save_outputs: bool = False,
) -> tuple[str, str]:
    """Synchronous wrapper around run_delivery_async."""
    return asyncio.run(
        run_delivery_async(
            feature_request,
            settings=settings,
            save_outputs=save_outputs,
        )
    )


# save_artifacts - write transcript.txt and delivery_report.md to disk
def save_artifacts(
    transcript: str,
    report: str,
    *,
    transcript_path: Path = TRANSCRIPT_PATH,
    report_path: Path = REPORT_PATH,
) -> None:
    """Write transcript.txt and delivery_report.md to disk."""
    transcript_path.write_text(transcript + "\n", encoding="utf-8")
    report_path.write_text(report + "\n", encoding="utf-8")
