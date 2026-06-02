# 02 — Lock (avoid race conditions)
# Run: python 02_thread_lock.py
#
# When two threads change shared data, results can be wrong without a lock.

from threading import Thread, Lock

counter = 0
lock = Lock()

def unsafe_increment():
    global counter
    for _ in range(100000):
        counter += 1

def safe_increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

# --- Demo safe version ---
counter = 0
threads = [Thread(target=safe_increment) for _ in range(2)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print("counter (with lock) =", counter)
