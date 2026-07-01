# 02 — Strings and counters
# Run: python 02_strings_counters.py

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from db_config import REDIS

import redis

PREFIX = "lesson:02:"

if __name__ == "__main__":
    r = redis.Redis(
        host=REDIS["host"],
        port=REDIS["port"],
        db=REDIS["db"],
        password=REDIS["password"],
        decode_responses=True,
    )
    r.set(f"{PREFIX}greeting", "Hello, Redis")
    print("GET:", r.get(f"{PREFIX}greeting"))

    r.incr(f"{PREFIX}page_views")
    r.incr(f"{PREFIX}page_views")
    print("INCR page_views:", r.get(f"{PREFIX}page_views"))

    r.delete(f"{PREFIX}greeting", f"{PREFIX}page_views")
