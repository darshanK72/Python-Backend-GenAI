"""Console output for SQL reflection traces."""

from __future__ import annotations


# print_question - print the question header
def print_question(question: str) -> None:
    """Print the question header."""
    print(f"\n{'=' * 60}")
    print("  Data Analytics Query Agent")
    print(f"{'=' * 60}")
    print(f"\nQuestion: {question}\n")


# print_generated_sql - print the SQL produced by the generator node
def print_generated_sql(sql: str) -> None:
    """Print the SQL produced by the generator node."""
    print("[generator] SQL:")
    print(f"  {sql}")
    print()


# print_validation - print whether validation passed or the rejection reason
def print_validation(is_valid: bool, error: str) -> None:
    """Print whether validation passed or the rejection reason."""
    if is_valid:
        print("[validator] SQL passed all checks\n")
    else:
        print(f"[validator] rejected: {error}\n")


# print_retry - print retry count and validator feedback sent to the generator
def print_retry(retry_count: int, error: str) -> None:
    """Print retry count and validator feedback sent to the generator."""
    print(f"[retry {retry_count}] validator feedback:")
    print(f"  {error}\n")


# print_answer - print the final formatted answer
def print_answer(answer: str) -> None:
    """Print the final formatted answer."""
    print("[answer]")
    for line in answer.splitlines():
        print(f"  {line}" if line else "")
    print()
