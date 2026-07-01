# 03 — Celery autoretry example
# Run: python 03_celery_autoretry.py

SNIPPET = '''
from celery_app import celery_app

@celery_app.task(bind=True, autoretry_for=(ConnectionError,), retry_backoff=True, max_retries=5)
def fetch_remote(self, url: str):
    ...
'''

if __name__ == "__main__":
    print("Celery autoretry snippet:\n", SNIPPET.strip())
