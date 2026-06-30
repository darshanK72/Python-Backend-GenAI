# 19 — Bridging blocking code into asyncio (run_in_executor)
# Run: python 19_asyncio_run_in_executor.py
#
# The golden rule of asyncio: NEVER call blocking code (time.sleep, heavy CPU
# loops, old synchronous libraries) directly inside a coroutine — it freezes
# the whole event loop. Instead, offload it to a thread or process pool and
# `await` the result. This combines async with the executors from lessons 10/14.
#   - blocking I/O  -> run in a thread pool
#   - blocking CPU  -> run in a process pool

import asyncio
import time
from concurrent.futures import ProcessPoolExecutor

def blocking_io(name):
    time.sleep(0.3)                  # a synchronous library call, can't be awaited
    return f"{name}: io done"

def cpu_heavy(n):
    return sum(i * i for i in range(n))

async def main():
    loop = asyncio.get_running_loop()

    # --- 1. Offload blocking I/O to the default thread pool ---
    # Passing None as the executor uses asyncio's built-in ThreadPoolExecutor.
    start = time.perf_counter()
    results = await asyncio.gather(
        loop.run_in_executor(None, blocking_io, "task-1"),
        loop.run_in_executor(None, blocking_io, "task-2"),
        loop.run_in_executor(None, blocking_io, "task-3"),
    )
    print("results:", results)
    print(f"3 blocking calls overlapped in {time.perf_counter() - start:.2f}s (~0.3s)")
    print("-" * 40)

    # --- 2. Offload CPU-bound work to a process pool ---
    # Keeps the event loop responsive while real parallel computing happens.
    with ProcessPoolExecutor() as pool:
        totals = await asyncio.gather(
            loop.run_in_executor(pool, cpu_heavy, 2_000_000),
            loop.run_in_executor(pool, cpu_heavy, 2_000_000),
        )
    print("cpu results (digit counts):", [len(str(t)) for t in totals])

    # --- 3. asyncio.to_thread: the modern shortcut (Python 3.9+) ---
    msg = await asyncio.to_thread(blocking_io, "shortcut")
    print("to_thread ->", msg)

if __name__ == "__main__":
    asyncio.run(main())
