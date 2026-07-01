# 01 — When to use a background job queue
# Run: python 01_when_to_queue.py

USE_QUEUE = [
    "Send email/SMS after signup",
    "Generate PDF or thumbnail",
    "Call slow third-party API",
    "Bulk data import/export",
    "Retry failed payments/webhooks",
]

KEEP_SYNC = [
    "Simple CRUD returning immediately",
    "Read from cache",
    "Validation and auth checks",
]

if __name__ == "__main__":
    print("Use a queue when work is slow, unreliable, or bursty:\n")
    for item in USE_QUEUE:
        print(f"  + {item}")
    print("\nKeep in request/response when fast and user needs instant answer:\n")
    for item in KEEP_SYNC:
        print(f"  - {item}")
