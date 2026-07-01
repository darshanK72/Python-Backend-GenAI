# 02 — Process pool for CPU-bound work
# Run: python 02_process_pool.py

from concurrent.futures import ProcessPoolExecutor


def cpu_heavy(n: int) -> int:
    return sum(i * i for i in range(n))


if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(cpu_heavy, [100_000, 200_000, 300_000]))
    print("Results:", results)
