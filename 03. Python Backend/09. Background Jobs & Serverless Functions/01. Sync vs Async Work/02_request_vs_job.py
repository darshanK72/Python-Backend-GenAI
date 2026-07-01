# 02 — Request/response vs fire-and-forget job
# Run: python 02_request_vs_job.py

import time
import uuid


def handle_signup_sync(email: str) -> dict:
  start = time.perf_counter()
  time.sleep(0.5)  # simulate slow email API
  return {"email": email, "elapsed_ms": int((time.perf_counter() - start) * 1000)}


def handle_signup_async(email: str) -> dict:
    job_id = str(uuid.uuid4())
    # In real app: enqueue send_welcome_email.delay(email)
    return {"email": email, "job_id": job_id, "status": "queued"}


if __name__ == "__main__":
    print("Sync:", handle_signup_sync("learner@example.com"))
    print("Async:", handle_signup_async("learner@example.com"))
