# 17 — asyncio synchronization & queues
# Run: python 17_asyncio_synchronization.py
#
# Even on one thread, async tasks interleave at every `await`, so you still
# need coordination tools. asyncio mirrors the threading ones — but you AWAIT
# them instead of blocking:
#   - asyncio.Lock      : one task in a critical section at a time
#   - asyncio.Semaphore : limit concurrency (e.g. max N requests at once)
#   - asyncio.Queue     : async producer/consumer pipeline

import asyncio

# --- 1. Lock: serialize access to shared state ---
async def lock_demo():
    lock = asyncio.Lock()
    balance = {"value": 0}

    async def deposit(amount):
        async with lock:
            current = balance["value"]
            await asyncio.sleep(0)        # yield: proves the lock holds across awaits
            balance["value"] = current + amount

    await asyncio.gather(*(deposit(10) for _ in range(5)))
    print("balance after 5 concurrent deposits:", balance["value"])

# --- 2. Semaphore: cap concurrent operations ---
async def semaphore_demo():
    sem = asyncio.Semaphore(2)           # at most 2 "downloads" at once
    active = {"n": 0}

    async def download(i):
        async with sem:
            active["n"] += 1
            print(f"download {i}: active now = {active['n']}")
            await asyncio.sleep(0.1)
            active["n"] -= 1

    await asyncio.gather(*(download(i) for i in range(5)))

# --- 3. Queue: producer feeds, consumers drain ---
async def queue_demo():
    queue = asyncio.Queue()

    async def producer():
        for i in range(5):
            await queue.put(i)
            await asyncio.sleep(0.02)
        await queue.put(None)            # sentinel to stop the consumer

    async def consumer():
        while True:
            item = await queue.get()
            if item is None:
                break
            print("consumed:", item * item)

    await asyncio.gather(producer(), consumer())

async def main():
    await lock_demo()
    print("-" * 40)
    await semaphore_demo()
    print("-" * 40)
    await queue_demo()

if __name__ == "__main__":
    asyncio.run(main())
