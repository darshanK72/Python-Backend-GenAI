# 09 — The GIL (Global Interpreter Lock), demonstrated
# Run: python 09_gil_explained.py
#
# CPython has ONE lock (the GIL) that lets only one thread execute Python
# bytecode at a time. Consequences:
#   - CPU-bound pure-Python code does NOT speed up with threads (often slower).
#   - I/O-bound code DOES benefit, because the GIL is released while waiting.
# True CPU parallelism in Python -> use multiprocessing (see lessons 11-14).

import time
from threading import Thread

# --- 1. CPU-bound work: threads do NOT help ---
def crunch(n):
    total = 0
    for i in range(n):
        total += i * i
    return total

N = 5_000_000

start = time.perf_counter()
crunch(N)
crunch(N)
sequential = time.perf_counter() - start
print(f"CPU-bound, sequential : {sequential:.2f}s")

start = time.perf_counter()
threads = [Thread(target=crunch, args=(N,)) for _ in range(2)]
for t in threads:
    t.start()
for t in threads:
    t.join()
threaded = time.perf_counter() - start
print(f"CPU-bound, 2 threads  : {threaded:.2f}s  (no faster — the GIL serializes it)")
print("-" * 40)

# --- 2. I/O-bound work: threads DO help ---
def wait_on_io():
    time.sleep(0.5)   # simulates a network/disk wait; GIL is released here

start = time.perf_counter()
wait_on_io()
wait_on_io()
print(f"I/O-bound, sequential : {time.perf_counter() - start:.2f}s  (~1.0s)")

start = time.perf_counter()
threads = [Thread(target=wait_on_io) for _ in range(2)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"I/O-bound, 2 threads  : {time.perf_counter() - start:.2f}s  (~0.5s — waits overlap)")

# --- 3. Takeaway ---
print()
print("Rule of thumb: threads for WAITING, processes for COMPUTING.")
