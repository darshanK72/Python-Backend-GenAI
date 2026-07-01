# 01 — Retry with exponential backoff
# Run: python 01_retry_pattern.py

import random
import time

MAX_RETRIES = 3


def flaky_api() -> str:
    if random.random() < 0.7:
        raise ConnectionError("temporary failure")
    return "ok"


def call_with_retry():
    delay = 1
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            return flaky_api()
        except ConnectionError as exc:
            print(f"attempt {attempt} failed: {exc}")
            if attempt == MAX_RETRIES:
                raise
            time.sleep(delay)
            delay *= 2


if __name__ == "__main__":
    random.seed(0)
    print("Result:", call_with_retry())
