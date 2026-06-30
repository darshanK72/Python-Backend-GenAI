# 11 — Multiprocessing basics (true parallelism)
# Run: python 11_multiprocessing_basics.py
#
# Each Process runs in its OWN interpreter with its OWN memory and its OWN GIL.
# That means real parallelism on multiple CPU cores — the way to speed up
# CPU-bound work in Python.
#
# IMPORTANT (Windows/macOS): child processes re-import this file, so all
# process-spawning code MUST live under `if __name__ == "__main__":`.

from multiprocessing import Process, current_process
import os
import time

def crunch(n, label):
    # Runs in a separate process with its own PID.
    total = sum(i * i for i in range(n))
    print(f"[{label}] pid={os.getpid()} total_digits={len(str(total))}")

if __name__ == "__main__":
    print(f"main process pid={os.getpid()}")

    # --- 1. Start two CPU-bound processes in parallel ---
    N = 5_000_000

    start = time.perf_counter()
    crunch(N, "sequential-a")
    crunch(N, "sequential-b")
    print(f"sequential: {time.perf_counter() - start:.2f}s")
    print("-" * 40)

    start = time.perf_counter()
    p1 = Process(target=crunch, args=(N, "proc-1"))
    p2 = Process(target=crunch, args=(N, "proc-2"))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(f"2 processes: {time.perf_counter() - start:.2f}s  (faster — real parallelism)")

    # --- 2. exitcode tells you how a process ended (0 = clean) ---
    print("proc-1 exitcode:", p1.exitcode)
