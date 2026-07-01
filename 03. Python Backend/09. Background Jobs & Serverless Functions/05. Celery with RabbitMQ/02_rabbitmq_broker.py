# 02 — Celery with RabbitMQ broker URL
# Run: python 02_rabbitmq_broker.py

import os

if __name__ == "__main__":
    os.environ.setdefault(
        "CELERY_BROKER_URL",
        "amqp://guest:guest@localhost:5672//",
    )
    print("Set broker:")
    print("  CELERY_BROKER_URL=amqp://guest:guest@localhost:5672//")
    print("Run worker:")
    print("  celery -A celery_app worker -l info")
    print("\nRequires RabbitMQ on localhost:5672")
