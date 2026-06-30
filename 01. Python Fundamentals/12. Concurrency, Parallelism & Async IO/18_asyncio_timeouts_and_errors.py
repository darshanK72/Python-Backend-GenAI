# 18 — asyncio timeouts & error handling
# Run: python 18_asyncio_timeouts_and_errors.py
#
# Real I/O can hang or fail. asyncio gives you tools to stay in control:
#   - asyncio.wait_for(coro, timeout) -> cancel and raise TimeoutError
#   - cancellation                    -> tasks can be cancelled cooperatively
#   - gather(..., return_exceptions=True) -> collect errors instead of crashing

import asyncio

async def slow_operation(seconds):
    try:
        await asyncio.sleep(seconds)
        return f"done in {seconds}s"
    except asyncio.CancelledError:
        # Good place to clean up before the task is torn down.
        print(f"slow_operation({seconds}s) was cancelled")
        raise

async def flaky(name, fail):
    await asyncio.sleep(0.1)
    if fail:
        raise RuntimeError(f"{name} failed")
    return f"{name} ok"

async def main():
    # --- 1. wait_for: enforce a deadline ---
    try:
        result = await asyncio.wait_for(slow_operation(1.0), timeout=0.3)
        print(result)
    except asyncio.TimeoutError:
        print("timed out -> operation cancelled automatically")
    print("-" * 40)

    # --- 2. Manual cancellation of a background task ---
    task = asyncio.create_task(slow_operation(5))
    await asyncio.sleep(0.1)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("main saw the task end as cancelled")
    print("-" * 40)

    # --- 3. gather with return_exceptions: one failure doesn't kill the rest ---
    results = await asyncio.gather(
        flaky("a", fail=False),
        flaky("b", fail=True),
        flaky("c", fail=False),
        return_exceptions=True,
    )
    for r in results:
        if isinstance(r, Exception):
            print("got error:", type(r).__name__, "-", r)
        else:
            print("got value:", r)

if __name__ == "__main__":
    asyncio.run(main())
