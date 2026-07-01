# 03 — Lists and sets
# Run: python 03_lists_and_sets.py

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from db_config import REDIS

import redis

PREFIX = "lesson:03:"

if __name__ == "__main__":
    r = redis.Redis(
        host=REDIS["host"],
        port=REDIS["port"],
        db=REDIS["db"],
        password=REDIS["password"],
        decode_responses=True,
    )

    queue = f"{PREFIX}queue"
    r.delete(queue)
    r.rpush(queue, "job-1", "job-2", "job-3")
    print("LPOP:", r.lpop(queue))
    print("Remaining list:", r.lrange(queue, 0, -1))

    tags = f"{PREFIX}tags"
    r.delete(tags)
    r.sadd(tags, "python", "redis", "python")
    print("SMEMBERS:", sorted(r.smembers(tags)))

    r.delete(queue, tags)
