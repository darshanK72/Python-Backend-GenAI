# 02 — Process one RQ job inline (no worker needed for demo)
# Run: python 02_rq_inline_demo.py

import time

from tasks import send_email


def run_inline():
    print("Running task synchronously (demo without Redis worker)...")
    result = send_email("learner@example.com", "Inline demo")
    print("Result:", result)


if __name__ == "__main__":
    run_inline()
