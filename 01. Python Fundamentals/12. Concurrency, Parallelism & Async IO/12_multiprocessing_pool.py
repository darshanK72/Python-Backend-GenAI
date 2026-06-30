# 12 — multiprocessing.Pool (parallel map over data)
# Run: python 12_multiprocessing_pool.py
#
# A Pool manages a fixed number of worker processes for you. You hand it a
# function and an iterable; it splits the work across cores and gathers results.
# This is the easiest way to parallelize "apply f to every item".

from multiprocessing import Pool, cpu_count
import time

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def heavy_square(x):
    time.sleep(0.1)        # simulate per-item CPU cost
    return x * x

if __name__ == "__main__":
    print("CPU cores available:", cpu_count())

    numbers = list(range(100_000, 100_020))

    # --- 1. pool.map(): blocking, results in order ---
    with Pool() as pool:
        flags = pool.map(is_prime, numbers)
    primes = [n for n, prime in zip(numbers, flags) if prime]
    print("primes found:", primes)
    print("-" * 40)

    # --- 2. Speedup vs sequential on artificial CPU work ---
    data = list(range(8))

    start = time.perf_counter()
    [heavy_square(x) for x in data]
    print(f"sequential map: {time.perf_counter() - start:.2f}s (~0.8s)")

    start = time.perf_counter()
    with Pool(processes=4) as pool:
        result = pool.map(heavy_square, data)
    print(f"pool map (4 procs): {time.perf_counter() - start:.2f}s -> {result}")

    # --- 3. starmap() for functions taking multiple arguments ---
    with Pool(2) as pool:
        sums = pool.starmap(pow, [(2, 3), (3, 2), (10, 2)])
    print("starmap pow results:", sums)
