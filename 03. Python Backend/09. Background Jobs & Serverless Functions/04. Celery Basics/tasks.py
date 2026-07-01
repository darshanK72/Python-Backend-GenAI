# Celery tasks

import time

from celery_app import celery_app


@celery_app.task(name="tasks.add")
def add(a: int, b: int) -> int:
    return a + b


@celery_app.task(name="tasks.send_report")
def send_report(user_id: int) -> dict:
    time.sleep(1)
    return {"user_id": user_id, "report": "generated"}
