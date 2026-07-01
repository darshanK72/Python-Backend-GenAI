# 01 — Celery configuration overview
# Run: python 01_celery_config.py

if __name__ == "__main__":
    print("Celery components:")
    print("  Broker   — Redis or RabbitMQ (message transport)")
    print("  Worker   — celery -A celery_app worker -l info")
    print("  Backend  — stores task results (optional)")
    print("  Beat     — scheduler for periodic tasks")
    print("\nEnqueue from Python:")
    print("  from tasks import add")
    print("  result = add.delay(2, 3)")
    print("  print(result.get(timeout=10))")
