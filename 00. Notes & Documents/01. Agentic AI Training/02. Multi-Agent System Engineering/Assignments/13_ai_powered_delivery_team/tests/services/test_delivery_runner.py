"""Tests for delivery orchestration."""

from __future__ import annotations

from unittest.mock import AsyncMock, patch

import pytest

from app.config import FEATURE_REQUEST
from app.services.delivery_runner import run_delivery_async, save_artifacts

# SAMPLE_TRANSCRIPT - minimal chat ending with the deployment token
SAMPLE_TRANSCRIPT = (
    "ProductOwner: criteria\n"
    "DevOps: DEPLOYMENT_COMPLETE: Task Notifications v1.0 deployed to staging"
)

# SAMPLE_REPORT - valid five-section delivery report
SAMPLE_REPORT = """# Delivery Report

## Executive Summary
Summary here.

## Technical Design
WebSockets design.

## Test Coverage
Five test cases listed.

## Deployment Configuration
Docker and health check.

## Open Questions
Retry policy question.
"""


# test_run_delivery_async_returns_transcript_and_report - test orchestration happy path
@pytest.mark.asyncio
async def test_run_delivery_async_returns_transcript_and_report(test_settings, tmp_path) -> None:
    with (
        patch(
            "app.services.delivery_runner.run_group_chat",
            new=AsyncMock(return_value=type("R", (), {"messages": []})()),
        ),
        patch(
            "app.services.delivery_runner.format_transcript",
            return_value=SAMPLE_TRANSCRIPT,
        ),
        patch(
            "app.services.delivery_runner.generate_delivery_report",
            new=AsyncMock(return_value=SAMPLE_REPORT),
        ),
    ):
        transcript, report = await run_delivery_async(
            FEATURE_REQUEST,
            settings=test_settings,
        )
    assert "DEPLOYMENT_COMPLETE" in transcript
    assert "Executive Summary" in report


# test_save_artifacts_writes_files - test transcript and report are written to disk
def test_save_artifacts_writes_files(tmp_path) -> None:
    transcript_path = tmp_path / "transcript.txt"
    report_path = tmp_path / "delivery_report.md"
    save_artifacts(
        "line one",
        "# Report",
        transcript_path=transcript_path,
        report_path=report_path,
    )
    assert transcript_path.read_text(encoding="utf-8").strip() == "line one"
    assert report_path.read_text(encoding="utf-8").strip() == "# Report"
