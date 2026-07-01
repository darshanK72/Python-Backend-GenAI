# 01 — Connect to Redis
# Run: python 01_connection.py
#
# Setup: Redis on localhost:6379, pip install redis

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from db_config import REDIS

try:
    import redis
except ImportError:
    print("Install: pip install redis")
    raise SystemExit(1)

if __name__ == "__main__":
    client = redis.Redis(
        host=REDIS["host"],
        port=REDIS["port"],
        db=REDIS["db"],
        password=REDIS["password"],
        decode_responses=True,
    )
    try:
        client.ping()
        print("Connected to Redis")
        print("SET/GET demo:", client.set("lesson:ping", "pong", ex=60))
        print("Value:", client.get("lesson:ping"))
    except redis.ConnectionError as e:
        print("Redis error:", e)
        print("Start Redis server and check .env settings.")
