# 10 — ThreadPoolExecutor (high-level threading)
# Run: python 10_thread_pool_executor.py
#
# concurrent.futures gives you a pool of worker threads and a clean API.
# You submit callables and get back Future objects (placeholders for results).
# This is the modern, preferred way to do threaded I/O work.

from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def fetch_user(user_id):
    time.sleep(0.2)                  # pretend this is a network call
    if user_id == 3:
        raise ValueError("user 3 not found")
    return {"id": user_id, "name": f"User{user_id}"}

ids = [1, 2, 3, 4, 5]

# --- 1. map(): simplest, results come back in input order ---
with ThreadPoolExecutor(max_workers=3) as pool:
    for uid, result in zip([1, 2, 4, 5], pool.map(fetch_user, [1, 2, 4, 5])):
        print("map ->", result)
print("-" * 40)

# --- 2. submit() + as_completed(): handle results as they finish ---
with ThreadPoolExecutor(max_workers=3) as pool:
    future_to_id = {pool.submit(fetch_user, uid): uid for uid in ids}
    for future in as_completed(future_to_id):
        uid = future_to_id[future]
        try:
            print("completed ->", future.result())   # re-raises worker errors here
        except ValueError as e:
            print(f"user {uid} failed:", e)
print("-" * 40)

# --- 3. Why it's faster: overlapping the waits ---
def timed_download(n):
    time.sleep(0.3)
    return n

start = time.perf_counter()
with ThreadPoolExecutor(max_workers=5) as pool:
    list(pool.map(timed_download, range(5)))
print(f"5 downloads with a pool: {time.perf_counter() - start:.2f}s (~0.3s, not 1.5s)")
