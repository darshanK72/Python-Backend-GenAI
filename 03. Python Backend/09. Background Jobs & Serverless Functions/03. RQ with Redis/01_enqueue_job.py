# 01 — Enqueue a job with RQ
# Run: python 01_enqueue_job.py
# Worker (separate terminal): rq worker --url redis://localhost:6379/0
# Install: pip install rq redis

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from db_config import REDIS

try:
    from redis import Redis
    from rq import Queue
except ImportError:
    print("Install: pip install rq redis")
    raise SystemExit(1)

from tasks import send_email


def get_queue() -> Queue:
    conn = Redis(
        host=REDIS["host"],
        port=REDIS["port"],
        db=REDIS["db"],
        password=REDIS["password"],
    )
    conn.ping()
    return Queue("lesson-emails", connection=conn)


if __name__ == "__main__":
    try:
        queue = get_queue()
        job = queue.enqueue(send_email, "learner@example.com", "Welcome!")
        print("Enqueued job id:", job.id)
        print("Check worker terminal for result.")
    except Exception as exc:
        print("Redis/RQ error:", exc)
        print("Start Redis, then: rq worker --url redis://localhost:6379/0")
