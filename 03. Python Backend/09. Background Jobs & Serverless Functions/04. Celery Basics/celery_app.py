# Celery application
# Broker: Redis (default). Run worker: celery -A celery_app worker -l info

import os

from celery import Celery

broker = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/1")
backend = os.getenv("CELERY_RESULT_BACKEND", broker)

celery_app = Celery("lesson_app", broker=broker, backend=backend)
celery_app.conf.task_serializer = "json"
celery_app.conf.result_serializer = "json"
celery_app.conf.accept_content = ["json"]
