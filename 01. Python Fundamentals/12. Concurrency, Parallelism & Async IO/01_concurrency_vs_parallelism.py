# 01 — Concurrency vs Parallelism (the big picture)
# Run: python 01_concurrency_vs_parallelism.py
#
# Three words people mix up:
#   - Concurrency : DEALING with many tasks at once (they make progress by
#                   taking turns). One cook switching between several dishes.
#   - Parallelism : DOING many tasks at the same instant on multiple CPU cores.
#                   Several cooks, one dish each.
#   - Async I/O   : a single thread juggling many tasks that mostly WAIT
#                   (network, disk). While one waits, another runs.
#
# Which Python tool fits which job:
#   - threading        -> concurrency for I/O-bound work (limited by the GIL)
#   - multiprocessing  -> true parallelism for CPU-bound work (separate cores)
#   - asyncio          -> concurrency for huge numbers of I/O waits, one thread

import time

# --- 1. CPU-bound vs I/O-bound: the key question ---
# Almost every "should I use threads or processes?" decision comes down to this.
def cpu_bound(n):
    # Pure Python number crunching: the CPU is busy the whole time.
    return sum(i * i for i in range(n))

def io_bound():
    # Waiting on something external: the CPU is mostly idle.
    time.sleep(0.2)
    return "data received"

print("CPU-bound result:", cpu_bound(100_000))
print("I/O-bound result:", io_bound())

# --- 2. Sequential baseline ---
# Run two I/O tasks one after another. Total time ~= sum of each wait.
start = time.perf_counter()
io_bound()
io_bound()
print("sequential 2x I/O:", round(time.perf_counter() - start, 2), "s (~0.4s)")

# --- 3. A simple mental model ---
print()
print("Decision guide:")
print("  Waiting a lot (web requests, files, DB)? -> threading or asyncio")
print("  Heavy math / data crunching in Python?    -> multiprocessing")
print("  Thousands of network calls at once?       -> asyncio")
print()
print("The next lessons show each tool in action.")
