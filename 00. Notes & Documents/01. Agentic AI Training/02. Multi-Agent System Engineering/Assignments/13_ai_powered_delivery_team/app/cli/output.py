"""Console output for the delivery team simulation."""

from __future__ import annotations


# print_feature_request - print the feature request kickoff header
def print_feature_request(request: str) -> None:
    """Print the feature request kickoff header."""
    print(f"\n{'=' * 60}")
    print("  AI-Powered Delivery Team")
    print(f"{'=' * 60}")
    print(f"\nFeature request:\n{request}\n")


# print_transcript - print the formatted group-chat transcript
def print_transcript(transcript: str) -> None:
    """Print the formatted group-chat transcript."""
    print("=== Group chat transcript ===\n")
    print(transcript)
    print()


# print_report - print the delivery_report.md content
def print_report(report: str) -> None:
    """Print the delivery_report.md content."""
    print("=== delivery_report.md ===\n")
    print(report)
    print()


# print_saved - print confirmation that an artifact was written to disk
def print_saved(path: str) -> None:
    """Print confirmation that an artifact was written to disk."""
    print(f"Saved {path}")
