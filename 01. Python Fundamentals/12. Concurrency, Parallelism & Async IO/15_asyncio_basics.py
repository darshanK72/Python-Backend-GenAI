# 15 — asyncio basics (async / await)
# Run: python 15_asyncio_basics.py
#
# asyncio runs many tasks on a SINGLE thread using cooperative multitasking.
#   - `async def` defines a coroutine.
#   - `await` pauses the coroutine and hands control back to the event loop,
#     so other coroutines can run while this one waits.
#   - `asyncio.run(main())` starts the event loop and runs until main() ends.
#
# Use it for I/O-bound work with lots of waiting (web APIs, sockets, DB).
# NOTE: `await asyncio.sleep(1)` yields to the loop; `time.sleep(1)` would
# block the whole loop and defeat the purpose.

import asyncio
import time

# --- 1. A coroutine that awaits ---
async def brew_coffee():
    print("coffee: started")
    await asyncio.sleep(0.3)        # non-blocking wait
    print("coffee: ready")
    return "coffee"

async def toast_bread():
    print("toast: started")
    await asyncio.sleep(0.2)
    print("toast: ready")
    return "toast"

# --- 2. Awaiting sequentially vs concurrently ---
async def main():
    # Sequential: each await finishes before the next starts.
    start = time.perf_counter()
    a = await brew_coffee()
    b = await toast_bread()
    print(f"sequential -> {a}, {b} in {time.perf_counter() - start:.2f}s (~0.5s)")
    print("-" * 40)

    # Concurrent: start both, then wait for both together.
    start = time.perf_counter()
    a, b = await asyncio.gather(brew_coffee(), toast_bread())
    print(f"concurrent -> {a}, {b} in {time.perf_counter() - start:.2f}s (~0.3s)")

# --- 3. Entry point ---
if __name__ == "__main__":
    asyncio.run(main())
