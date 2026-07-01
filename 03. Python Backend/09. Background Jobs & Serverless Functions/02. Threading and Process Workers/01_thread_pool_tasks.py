# 01 — Thread pool for light background work
# Run: python 01_thread_pool_tasks.py

import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def send_notification(user_id: int) -> str:
    time.sleep(0.2)
    return f"notified user {user_id}"


if __name__ == "__main__":
    user_ids = [1, 2, 3, 4]
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = [pool.submit(send_notification, uid) for uid in user_ids]
        for f in as_completed(futures):
            print(f.result())
