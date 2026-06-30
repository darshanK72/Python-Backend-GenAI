# 07 — Semaphore (limit how many threads run at once)
# Run: python 07_semaphore.py
#
# A Semaphore holds a counter. acquire() decrements (blocking at 0),
# release() increments. Perfect for limiting concurrency, e.g. "at most
# 3 downloads / DB connections at a time".

from threading import Thread, Semaphore, BoundedSemaphore
import time

# --- 1. Allow at most 2 workers in the "pool" simultaneously ---
pool = Semaphore(2)

def access_resource(worker_id):
    print(f"worker {worker_id}: waiting for a slot")
    with pool:                       # acquire on enter, release on exit
        print(f"worker {worker_id}: >>> using resource")
        time.sleep(0.4)
        print(f"worker {worker_id}: <<< done, freeing slot")

workers = [Thread(target=access_resource, args=(i,)) for i in range(5)]
for w in workers:
    w.start()
for w in workers:
    w.join()
print("-" * 30)

# --- 2. BoundedSemaphore: catches release() bugs ---
# A BoundedSemaphore raises ValueError if you release more times than you
# acquired, which catches a common mistake a plain Semaphore would hide.
bounded = BoundedSemaphore(1)
bounded.acquire()
bounded.release()
try:
    bounded.release()                # one too many!
except ValueError as e:
    print("BoundedSemaphore caught extra release:", e)
