# 06 — Cache-aside pattern
# Run: python 06_cache_aside.py

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from db_config import REDIS

import redis

CACHE_KEY = "lesson:06:product:42"


def fetch_product_from_db(product_id: int) -> dict:
    print("(simulated DB query)")
    return {"id": product_id, "name": "Notebook", "price": 120}


def get_product(r: redis.Redis, product_id: int) -> dict:
    cached = r.get(CACHE_KEY)
    if cached:
        print("Cache hit")
        return json.loads(cached)

    print("Cache miss")
    product = fetch_product_from_db(product_id)
    r.set(CACHE_KEY, json.dumps(product), ex=60)
    return product


if __name__ == "__main__":
    r = redis.Redis(
        host=REDIS["host"],
        port=REDIS["port"],
        db=REDIS["db"],
        password=REDIS["password"],
        decode_responses=True,
    )
    r.delete(CACHE_KEY)

    print("First call:", get_product(r, 42))
    print("Second call:", get_product(r, 42))

    r.delete(CACHE_KEY)
