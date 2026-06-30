"""Temporary: validate notebook JSON and confirm reference solutions pass."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

for name in ["17_concurrency_and_async_practice.ipynb", "18_unit_testing_practice.ipynb"]:
    with open(os.path.join(HERE, name), encoding="utf-8") as f:
        nb = json.load(f)
    assert nb["nbformat"] == 4
    print(name, "-> valid JSON,", len(nb["cells"]), "cells")

print("\n--- exercising reference solutions ---")

import asyncio
import threading
import queue
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Thread, Lock


def run_async(coro):
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        return asyncio.run(coro)
    result = {}

    def _runner():
        result["value"] = asyncio.run(coro)

    t = threading.Thread(target=_runner)
    t.start()
    t.join()
    return result["value"]


# NB17 P1
def square_all(nums):
    with ThreadPoolExecutor() as pool:
        return list(pool.map(lambda n: n * n, nums))


assert square_all([1, 2, 3, 4]) == [1, 4, 9, 16]
assert square_all([]) == []

# NB17 P2
def count_up(num_threads, per_thread):
    total = {"v": 0}
    lock = Lock()

    def work():
        for _ in range(per_thread):
            with lock:
                total["v"] += 1

    ts = [Thread(target=work) for _ in range(num_threads)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    return total["v"]


assert count_up(4, 1000) == 4000

# NB17 P3
def process_items(items):
    q = queue.Queue()
    for it in items:
        q.put(it)
    results = queue.Queue()

    def worker():
        while True:
            try:
                it = q.get_nowait()
            except queue.Empty:
                return
            results.put(it * it)
            q.task_done()

    ts = [Thread(target=worker) for _ in range(3)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    return sum(results.queue)


assert process_items([1, 2, 3]) == 14
assert process_items(list(range(1, 6))) == 55

# NB17 P4
def fetch_lengths(words):
    out = {}
    with ThreadPoolExecutor(max_workers=4) as pool:
        futs = {pool.submit(lambda w: (w, len(w)), w): w for w in words}
        for fut in as_completed(futs):
            w, n = fut.result()
            out[w] = n
    return out


assert fetch_lengths(["a", "bb", "ccc"]) == {"a": 1, "bb": 2, "ccc": 3}
assert fetch_lengths([]) == {}

# NB17 P5
async def fetch(n):
    await asyncio.sleep(0)
    return n * 2


async def double_all(nums):
    return await asyncio.gather(*(fetch(n) for n in nums))


assert run_async(double_all([1, 2, 3])) == [2, 4, 6]

# NB17 P6
async def guard(coro, limit):
    try:
        return await asyncio.wait_for(coro, limit)
    except asyncio.TimeoutError:
        return "timeout"


async def quick():
    await asyncio.sleep(0.01)
    return "done"


async def slow():
    await asyncio.sleep(1)
    return "done"


assert run_async(guard(quick(), 0.5)) == "done"
assert run_async(guard(slow(), 0.1)) == "timeout"

# NB17 P7
def best_tool(workload):
    return {"cpu": "multiprocessing", "io_few": "threading", "io_many": "asyncio"}[workload]


assert best_tool("cpu") == "multiprocessing"

print("NB17 solutions: all assertions passed")


# NB18 P1
def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b


assert divide(10, 2) == 5.0
try:
    divide(1, 0)
except ValueError as e:
    assert str(e) == "cannot divide by zero"

# NB18 P2
def assert_raises(fn, exc):
    try:
        fn()
    except exc:
        return True
    except Exception:
        return False
    return False


assert assert_raises(lambda: 1 / 0, ZeroDivisionError) is True
assert assert_raises(lambda: 1 + 1, ZeroDivisionError) is False
assert assert_raises(lambda: 1 / 0, ValueError) is False

# NB18 P3
def run_cases(func, cases):
    return sum(1 for args, expected in cases if func(*args) == expected)


assert run_cases(lambda x: x * 2, [((2,), 4), ((3,), 6)]) == 2
assert run_cases(lambda x: x * 2, [((2,), 4), ((3,), 99)]) == 1
assert run_cases(lambda a, b: a + b, [((1, 2), 3), ((5, 5), 10)]) == 2

# NB18 P4
import unittest


class TestDivide(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(divide(10, 2), 5.0)

    def test_zero(self):
        with self.assertRaises(ValueError):
            divide(1, 0)


suite = unittest.TestLoader().loadTestsFromTestCase(TestDivide)
result = unittest.TextTestRunner(verbosity=0).run(suite)
assert result.wasSuccessful()

# NB18 P5
def get_username(client, user_id):
    return client.fetch(user_id)["name"]


from unittest.mock import Mock, patch

client = Mock()
client.fetch.return_value = {"name": "Asha", "id": 7}
assert get_username(client, 7) == "Asha"
assert client.fetch.call_args.args == (7,)

# NB18 P6
from datetime import datetime


def now():
    return datetime.now()


def is_weekend():
    return now().weekday() in (5, 6)


with patch("__main__.now", return_value=datetime(2024, 1, 6)):
    assert is_weekend() is True
with patch("__main__.now", return_value=datetime(2024, 1, 3)):
    assert is_weekend() is False

print("NB18 solutions: all assertions passed")
print("\nALL GOOD")
