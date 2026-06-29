# 01 — Context managers and contextlib
# Run: python 01_context_managers.py
#
# Objects used with 'with' implement __enter__ and __exit__.

from contextlib import contextmanager
import os

# --- 1. File is a context manager (already known) ---
path = "ctx_demo.txt"
with open(path, "w", encoding="utf-8") as f:
    f.write("data")
os.remove(path)

# --- 2. Custom class ---
class Timer:
    def __enter__(self):
        import time
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        elapsed = time.perf_counter() - self.start
        print(f"Elapsed: {elapsed:.4f}s")
        return False   # do not suppress exceptions

with Timer():
    total = sum(range(100000))
    print("total computed")

# --- 3. @contextmanager decorator ---
@contextmanager
def tag(name):
    print(f"[{name}] start")
    try:
        yield name
    finally:
        print(f"[{name}] end")

with tag("job") as label:
    print("working in", label)
