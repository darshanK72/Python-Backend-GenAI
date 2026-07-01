# 01 — Simple in-memory rate limiting
# Run: python 01_rate_limiting.py

import time
from collections import defaultdict

WINDOW_SECONDS = 60
MAX_REQUESTS = 5
_buckets: dict[str, list[float]] = defaultdict(list)


def allow_request(client_id: str) -> bool:
    now = time.time()
    window_start = now - WINDOW_SECONDS
    hits = [t for t in _buckets[client_id] if t >= window_start]
    if len(hits) >= MAX_REQUESTS:
        _buckets[client_id] = hits
        return False
    hits.append(now)
    _buckets[client_id] = hits
    return True


if __name__ == "__main__":
    client = "192.168.1.10"
    for i in range(7):
        ok = allow_request(client)
        print(f"Request {i + 1}:", "allowed" if ok else "rate limited")
