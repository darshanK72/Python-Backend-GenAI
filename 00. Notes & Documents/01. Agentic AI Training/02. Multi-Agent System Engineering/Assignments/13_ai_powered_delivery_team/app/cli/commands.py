"""CLI command handlers."""

from __future__ import annotations

import sys

from app.cli.output import print_feature_request, print_report, print_saved, print_transcript
from app.config import FEATURE_REQUEST, REPORT_PATH, TRANSCRIPT_PATH
from app.services.delivery_runner import run_delivery


# run_simulation - execute the delivery team chat and print transcript + report
def run_simulation(
    feature_request: str = FEATURE_REQUEST,
    *,
    save_outputs: bool = False,
) -> tuple[str, str]:
    """Run the delivery team simulation and print outputs."""
    print_feature_request(feature_request)
    transcript, report = run_delivery(feature_request, save_outputs=save_outputs)
    print_transcript(transcript)
    print_report(report)
    if save_outputs:
        print_saved(str(TRANSCRIPT_PATH))
        print_saved(str(REPORT_PATH))
    return transcript, report


# cmd_run - run the simulation and return an exit code
def cmd_run(
    feature_request: str = FEATURE_REQUEST,
    *,
    save_outputs: bool = False,
) -> int:
    """Run the delivery simulation and return an exit code."""
    try:
        run_simulation(feature_request, save_outputs=save_outputs)
    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0
