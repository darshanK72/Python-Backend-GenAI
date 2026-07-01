# 02 — Celery Beat for cron-style jobs
# Run: python 02_celery_beat_overview.py

BEAT_CONFIG = """
# celery_app.py
celery_app.conf.beat_schedule = {
    'daily-report': {
        'task': 'tasks.send_report',
        'schedule': 60.0,  # every 60 seconds (demo)
        'args': (1,),
    },
}

# Run scheduler:
#   celery -A celery_app beat -l info
# Run worker:
#   celery -A celery_app worker -l info
"""

if __name__ == "__main__":
    print("Celery Beat = cron for distributed workers\n")
    print(BEAT_CONFIG.strip())
