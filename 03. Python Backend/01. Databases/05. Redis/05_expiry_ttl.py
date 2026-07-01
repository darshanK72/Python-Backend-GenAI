# 05 — Expiry (TTL)
# Run: python 05_expiry_ttl.py

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from db_config import REDIS

import redis

KEY = "lesson:05:otp"

if __name__ == "__main__":
    r = redis.Redis(
        host=REDIS["host"],
        port=REDIS["port"],
        db=REDIS["db"],
        password=REDIS["password"],
        decode_responses=True,
    )
    r.set(KEY, "123456", ex=3)
    print("TTL seconds:", r.ttl(KEY))
    print("Value now:", r.get(KEY))
    time.sleep(3)
    print("Value after expiry:", r.get(KEY))
