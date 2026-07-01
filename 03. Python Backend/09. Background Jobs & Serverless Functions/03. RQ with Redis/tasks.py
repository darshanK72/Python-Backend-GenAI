# RQ task definitions
# Used by 01_enqueue_job.py and rq worker

import time


def send_email(to: str, subject: str) -> dict:
    time.sleep(1)
    return {"to": to, "subject": subject, "status": "sent"}
