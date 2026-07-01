# 03 — Timing-safe comparison (avoid leaking secrets via timing)
# Run: python 03_timing_safe_compare.py

import secrets


def unsafe_compare(a: str, b: str) -> bool:
    return a == b


def safe_compare(a: str, b: str) -> bool:
    return secrets.compare_digest(a.encode(), b.encode())


if __name__ == "__main__":
    token = "super-secret-api-token"
    print("Unsafe match:", unsafe_compare(token, "super-secret-api-token"))
    print("Safe match:", safe_compare(token, "super-secret-api-token"))
    print("Safe reject:", safe_compare(token, "wrong-token"))
    print("\nUse secrets.compare_digest for API keys, tokens, and password hashes.")
