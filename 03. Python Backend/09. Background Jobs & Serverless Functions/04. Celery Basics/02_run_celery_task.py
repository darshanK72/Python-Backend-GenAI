# 02 — Call a Celery task (requires Redis + worker)
# Run: python 02_run_celery_task.py
# Worker: celery -A celery_app worker -l info  (from this folder)

import sys

try:
    from tasks import add, send_report
except ImportError:
    print("Run from 04. Celery Basics folder")
    raise SystemExit(1)


if __name__ == "__main__":
    try:
        async_result = add.delay(10, 32)
        print("add task id:", async_result.id)
        print("result:", async_result.get(timeout=15))

        report = send_report.delay(42)
        print("report:", report.get(timeout=15))
    except Exception as exc:
        print("Celery error:", exc)
        print("Start Redis, then: celery -A celery_app worker -l info")
