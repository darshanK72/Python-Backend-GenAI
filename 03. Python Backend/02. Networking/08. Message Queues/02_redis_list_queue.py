# 02 — Redis list as a simple queue (LPUSH / BRPOP)
# Run: python 02_redis_list_queue.py

import sys
import threading
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from db_config import REDIS

import redis

QUEUE = "lesson:task_queue"


def worker(client: redis.Redis):
    print("Worker waiting for jobs...")
    while True:
        item = client.brpop(QUEUE, timeout=5)
        if not item:
            break
        _, job = item
        print("Processed job:", job)
        if job == "STOP":
            break


if __name__ == "__main__":
    r = redis.Redis(
        host=REDIS["host"],
        port=REDIS["port"],
        db=REDIS["db"],
        password=REDIS["password"],
        decode_responses=True,
    )
    r.delete(QUEUE)

    thread = threading.Thread(target=worker, args=(r,), daemon=True)
    thread.start()
    time.sleep(0.3)

    for job_id in ["email-1", "email-2", "STOP"]:
        r.lpush(QUEUE, job_id)
        print("Enqueued:", job_id)
        time.sleep(0.2)

    thread.join(timeout=10)
