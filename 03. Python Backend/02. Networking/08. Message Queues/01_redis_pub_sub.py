# 01 — Redis pub/sub
# Run: python 01_redis_pub_sub.py
# Requires Redis on localhost (see 01. Databases/06. Redis)

import sys
import threading
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from db_config import REDIS

try:
    import redis
except ImportError:
    print("Install: pip install redis")
    raise SystemExit(1)

CHANNEL = "lesson:orders"


def subscriber(client: redis.Redis):
    pubsub = client.pubsub()
    pubsub.subscribe(CHANNEL)
    print("Subscriber listening...")
    for message in pubsub.listen():
        if message["type"] == "message":
            print("Received:", message["data"])
            if message["data"] == "done":
                break
    pubsub.close()


if __name__ == "__main__":
    r = redis.Redis(
        host=REDIS["host"],
        port=REDIS["port"],
        db=REDIS["db"],
        password=REDIS["password"],
        decode_responses=True,
    )
    try:
        r.ping()
    except redis.ConnectionError as e:
        print("Redis error:", e)
        raise SystemExit(1)

    thread = threading.Thread(target=subscriber, args=(r,), daemon=True)
    thread.start()
    time.sleep(0.5)

    r.publish(CHANNEL, "order-created:#1001")
    r.publish(CHANNEL, "order-created:#1002")
    r.publish(CHANNEL, "done")
    thread.join(timeout=3)
