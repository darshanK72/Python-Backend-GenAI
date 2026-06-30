# 14 — ProcessPoolExecutor (high-level parallelism)
# Run: python 14_process_pool_executor.py
#
# Same concurrent.futures API as ThreadPoolExecutor (lesson 10), but backed by
# PROCESSES — so it gives true CPU parallelism. Swapping one for the other is
# often a one-line change, which makes it easy to pick the right backend.

from concurrent.futures import ProcessPoolExecutor, as_completed
import time

def count_primes_up_to(limit):
    # A genuinely CPU-bound task, good for measuring real parallel speedup.
    count = 0
    for n in range(2, limit):
        is_prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return limit, count

if __name__ == "__main__":
    limits = [50_000, 60_000, 70_000, 80_000]

    # --- 1. Sequential baseline ---
    start = time.perf_counter()
    sequential = [count_primes_up_to(n) for n in limits]
    print(f"sequential: {time.perf_counter() - start:.2f}s -> {sequential}")
    print("-" * 40)

    # --- 2. Parallel with a process pool ---
    start = time.perf_counter()
    with ProcessPoolExecutor() as pool:
        parallel = list(pool.map(count_primes_up_to, limits))
    print(f"process pool: {time.perf_counter() - start:.2f}s -> {parallel}")
    print("-" * 40)

    # --- 3. submit() + as_completed() with error handling ---
    with ProcessPoolExecutor(max_workers=2) as pool:
        futures = [pool.submit(count_primes_up_to, n) for n in limits]
        for future in as_completed(futures):
            limit, count = future.result()
            print(f"up to {limit}: {count} primes")
