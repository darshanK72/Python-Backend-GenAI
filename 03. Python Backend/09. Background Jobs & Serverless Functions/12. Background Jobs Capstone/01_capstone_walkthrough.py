# 01 — Background jobs capstone walkthrough
# Run: python 01_capstone_walkthrough.py

if __name__ == "__main__":
    print("Capstone flow:")
    print("  1. uvicorn app:app --port 8020")
    print('  2. POST /signup {"email":"learner@example.com"}')
    print("  3. GET /jobs/{job_id}")
    print("\nExtend with RQ/Celery:")
    print("  Replace enqueue_welcome_email with queue.enqueue(...)")
