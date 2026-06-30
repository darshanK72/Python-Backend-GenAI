# 16 — asyncio Tasks and gather
# Run: python 16_asyncio_tasks_and_gather.py
#
# A coroutine doesn't run until something awaits it. A Task wraps a coroutine
# and SCHEDULES it on the event loop immediately, so it starts running in the
# background while you do other work.
#   - asyncio.create_task(coro)  -> schedule now, await later
#   - asyncio.gather(*coros)     -> run many concurrently, collect results
#   - asyncio.as_completed(...)  -> handle results in finish order

import asyncio

async def fetch(name, delay):
    await asyncio.sleep(delay)
    return f"{name} (after {delay}s)"

# --- 1. create_task: work starts in the background ---
async def with_tasks():
    task1 = asyncio.create_task(fetch("alpha", 0.3))
    task2 = asyncio.create_task(fetch("beta", 0.1))
    # Both are already running here; we can do other work before awaiting.
    print("tasks scheduled, doing other setup...")
    print("got:", await task1)
    print("got:", await task2)

# --- 2. gather: wait for many at once, results in submission order ---
async def with_gather():
    results = await asyncio.gather(
        fetch("one", 0.3),
        fetch("two", 0.1),
        fetch("three", 0.2),
    )
    print("gather results:", results)

# --- 3. as_completed: react as each finishes (fastest first) ---
async def with_as_completed():
    coros = [fetch("slow", 0.3), fetch("fast", 0.1), fetch("medium", 0.2)]
    for coro in asyncio.as_completed(coros):
        print("finished:", await coro)

async def main():
    await with_tasks()
    print("-" * 40)
    await with_gather()
    print("-" * 40)
    await with_as_completed()

if __name__ == "__main__":
    asyncio.run(main())
