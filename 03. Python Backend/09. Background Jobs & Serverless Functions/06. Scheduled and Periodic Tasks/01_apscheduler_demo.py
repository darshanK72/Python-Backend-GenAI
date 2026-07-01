# 01 — Periodic tasks with APScheduler
# Run: python 01_apscheduler_demo.py
# Install: pip install apscheduler

import time

try:
    from apscheduler.schedulers.background import BackgroundScheduler
except ImportError:
    print("Install: pip install apscheduler")
    raise SystemExit(1)


def heartbeat():
    print("scheduled heartbeat", flush=True)


if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    scheduler.add_job(heartbeat, "interval", seconds=2, id="heartbeat")
    scheduler.start()
    print("Scheduler running 5 seconds...")
    time.sleep(5)
    scheduler.shutdown()
    print("Done.")
