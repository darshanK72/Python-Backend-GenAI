# 04 — Hashes (objects / dictionaries)
# Run: python 04_hashes.py

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from db_config import REDIS

import redis

KEY = "lesson:04:user:1"

if __name__ == "__main__":
    r = redis.Redis(
        host=REDIS["host"],
        port=REDIS["port"],
        db=REDIS["db"],
        password=REDIS["password"],
        decode_responses=True,
    )
    r.delete(KEY)
    r.hset(KEY, mapping={"name": "Asha", "city": "Pune", "role": "learner"})
    print("HGETALL:", r.hgetall(KEY))
    print("HGET name:", r.hget(KEY, "name"))
    r.delete(KEY)
