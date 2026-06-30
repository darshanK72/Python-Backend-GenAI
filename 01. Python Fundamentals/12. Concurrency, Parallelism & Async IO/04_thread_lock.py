# 04 — Lock: avoiding race conditions
# Run: python 04_thread_lock.py
#
# When several threads modify the same data, "counter += 1" is NOT atomic:
# read -> add -> write. Two threads can interleave and lose updates.
# A Lock makes a section run by only one thread at a time.

from threading import Thread, Lock

# --- 1. The problem: an unsafe shared counter ---
def make_counter():
    return {"value": 0}

def unsafe_increment(counter, times):
    for _ in range(times):
        counter["value"] += 1   # race condition under heavy contention

counter = make_counter()
threads = [Thread(target=unsafe_increment, args=(counter, 100_000)) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print("unsafe counter (expected 400000):", counter["value"])

# --- 2. The fix: protect the shared write with a Lock ---
lock = Lock()

def safe_increment(counter, times):
    for _ in range(times):
        with lock:                 # only one thread inside at a time
            counter["value"] += 1

counter = make_counter()
threads = [Thread(target=safe_increment, args=(counter, 100_000)) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print("safe counter   (expected 400000):", counter["value"])

# --- 3. Lock as a guard around a critical section ---
# acquire()/release() is the manual form; "with lock" is preferred because it
# always releases, even if an exception is raised inside the block.
balance = 100
balance_lock = Lock()

def withdraw(amount):
    global balance
    with balance_lock:
        if balance >= amount:
            balance -= amount

ts = [Thread(target=withdraw, args=(30,)) for _ in range(5)]
for t in ts:
    t.start()
for t in ts:
    t.join()
print("final balance after 5x withdraw(30):", balance)
