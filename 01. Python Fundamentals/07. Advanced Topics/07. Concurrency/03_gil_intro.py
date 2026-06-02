# 03 — GIL (Global Interpreter Lock) — concept
# Run: python 03_gil_intro.py
#
# CPython allows only one thread to execute Python bytecode at a time.
# So threads do not speed up CPU-bound pure Python code much.
# They still help when threads wait on I/O.

print("GIL summary:")
print("- I/O-bound (downloads, DB, files) -> threading can help")
print("- CPU-bound (heavy math in Python) -> use multiprocessing or C extensions")
print("- For learning and small scripts, threading is fine for background tasks")

# --- Simple CPU vs I/O analogy ---
import time
from threading import Thread

def io_style():
    time.sleep(0.5)
    print("io_style done")

def cpu_style():
    total = sum(i * i for i in range(2_000_00))
    print("cpu_style done, total digits:", len(str(total)))

start = time.perf_counter()
threads = [Thread(target=io_style) for _ in range(2)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print("2 io threads elapsed:", round(time.perf_counter() - start, 2), "s (about 0.5s)")
