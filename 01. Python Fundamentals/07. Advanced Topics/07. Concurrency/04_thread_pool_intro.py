# 04 — ThreadPoolExecutor (high-level threading)
# Run: python 04_thread_pool_intro.py

from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def fetch_data(user_id):
    time.sleep(0.2)
    return {"user_id": user_id, "name": f"User{user_id}"}

ids = [1, 2, 3, 4, 5]

# --- 1. map style ---
with ThreadPoolExecutor(max_workers=3) as pool:
    results = list(pool.map(fetch_data, ids))
print("map results:", results)

# --- 2. submit + as_completed ---
with ThreadPoolExecutor(max_workers=3) as pool:
    futures = [pool.submit(fetch_data, i) for i in ids]
    for future in as_completed(futures):
        print("got:", future.result())
