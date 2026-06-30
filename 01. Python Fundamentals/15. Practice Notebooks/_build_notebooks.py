"""Temporary builder: generates two practice notebooks with valid JSON.

Run once, then delete this file. Avoids manual JSON escaping of code that
contains quotes, f-strings and emoji.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

KERNEL_META = {
    "kernelspec": {"display_name": ".venv", "language": "python", "name": "python3"},
    "language_info": {
        "codemirror_mode": {"name": "ipython", "version": 3},
        "file_extension": ".py",
        "mimetype": "text/x-python",
        "name": "python",
        "nbconvert_exporter": "python",
        "pygments_lexer": "ipython3",
        "version": "3.13.7",
    },
}


def md(text):
    return {"cell_type": "markdown", "metadata": {}, "source": text}


def code(text):
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": text,
    }


def write_notebook(filename, cells):
    nb = {
        "cells": cells,
        "metadata": KERNEL_META,
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    path = os.path.join(HERE, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("wrote", filename)


HELPERS = '''# Run this cell once per notebook — provides test validation helpers.
import asyncio
import threading


def check_equal(name, actual, expected):
    """Compare actual vs expected; print pass/fail."""
    if actual == expected:
        print(f"\u2713 {name}")
        return True
    print(f"\u2717 {name}")
    print(f"  Expected: {expected!r}")
    print(f"  Got:      {actual!r}")
    return False


def run_tests(cases):
    """Run a list of (name, callable) tuples. Callable should return the answer."""
    passed = 0
    for name, fn in cases:
        try:
            if check_equal(name, fn(), True):
                passed += 1
        except Exception as exc:
            print(f"\u2717 {name} \u2014 Error: {type(exc).__name__}: {exc}")
    total = len(cases)
    print(f"\\nResult: {passed}/{total} passed")
    if passed == total:
        print("\U0001f389 All tests passed!")
    return passed == total


def run_async(coro):
    """Run a coroutine safely, even inside a notebook's running event loop."""
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
'''

# ---------------------------------------------------------------------------
# Notebook 17: Concurrency, Parallelism & Async IO
# ---------------------------------------------------------------------------
nb17 = [
    md(
        "# Practice: Concurrency, Parallelism & Async IO\n"
        "\n"
        "Write your solutions in the **YOUR CODE** cells, then run **Validate** cells.\n"
        "\n"
        "These problems focus on `threading`, `concurrent.futures` and `asyncio` "
        "(they all run cleanly inside a notebook). `multiprocessing` is covered "
        "conceptually in the final problem, since spawning real processes from a "
        "notebook is unreliable on Windows."
    ),
    code(HELPERS),

    md(
        "---\n"
        "\n"
        "## Problem 1: parallel squares `Easy`\n"
        "\n"
        "Using `ThreadPoolExecutor`, define `square_all(nums)` that returns a list of "
        "each number squared, in the **same order** as the input. Use the pool's `map`.\n"
        "\n"
        "**Examples**\n"
        "\n"
        "```\n"
        "square_all([1, 2, 3, 4]) \u2192 [1, 4, 9, 16]\n"
        "```"
    ),
    code(
        "# YOUR CODE\n"
        "from concurrent.futures import ThreadPoolExecutor\n"
        "\n"
        "def square_all(nums):\n"
        "    pass\n"
    ),
    code(
        "check_equal('basic', square_all([1, 2, 3, 4]), [1, 4, 9, 16])\n"
        "check_equal('order', square_all([5, 1, 3]), [25, 1, 9])\n"
        "check_equal('empty', square_all([]), [])\n"
    ),

    md(
        "---\n"
        "\n"
        "## Problem 2: thread-safe counter `Medium`\n"
        "\n"
        "Define `count_up(num_threads, per_thread)` that starts `num_threads` threads, "
        "each incrementing a **shared** counter `per_thread` times. Protect the "
        "increment with a `Lock` so no updates are lost, then return the final total.\n"
        "\n"
        "**Examples**\n"
        "\n"
        "```\n"
        "count_up(4, 1000) \u2192 4000\n"
        "```"
    ),
    code(
        "# YOUR CODE\n"
        "from threading import Thread, Lock\n"
        "\n"
        "def count_up(num_threads, per_thread):\n"
        "    pass\n"
    ),
    code(
        "check_equal('4x1000', count_up(4, 1000), 4000)\n"
        "check_equal('2x5000', count_up(2, 5000), 10000)\n"
    ),

    md(
        "---\n"
        "\n"
        "## Problem 3: worker queue `Medium`\n"
        "\n"
        "Using `queue.Queue` and a few worker threads, define `process_items(items)` "
        "where each worker computes the square of an item. Return the **sum** of all "
        "squares. Order doesn't matter, but every item must be processed exactly once.\n"
        "\n"
        "**Examples**\n"
        "\n"
        "```\n"
        "process_items([1, 2, 3]) \u2192 14   # 1 + 4 + 9\n"
        "```"
    ),
    code(
        "# YOUR CODE\n"
        "from threading import Thread\n"
        "import queue\n"
        "\n"
        "def process_items(items):\n"
        "    pass\n"
    ),
    code(
        "check_equal('small', process_items([1, 2, 3]), 14)\n"
        "check_equal('range', process_items(list(range(1, 6))), 55)\n"
    ),

    md(
        "---\n"
        "\n"
        "## Problem 4: gather results `Medium`\n"
        "\n"
        "Using `ThreadPoolExecutor.submit` and `as_completed`, define "
        "`fetch_lengths(words)` that returns a dict mapping each word to its length "
        "(pretend each lookup is slow I/O done in a thread).\n"
        "\n"
        "**Examples**\n"
        "\n"
        "```\n"
        "fetch_lengths(['a', 'bb', 'ccc']) \u2192 {'a': 1, 'bb': 2, 'ccc': 3}\n"
        "```"
    ),
    code(
        "# YOUR CODE\n"
        "from concurrent.futures import ThreadPoolExecutor, as_completed\n"
        "\n"
        "def fetch_lengths(words):\n"
        "    pass\n"
    ),
    code(
        "check_equal('basic', fetch_lengths(['a', 'bb', 'ccc']), {'a': 1, 'bb': 2, 'ccc': 3})\n"
        "check_equal('empty', fetch_lengths([]), {})\n"
    ),

    md(
        "---\n"
        "\n"
        "## Problem 5: async gather `Medium`\n"
        "\n"
        "Complete the coroutine `fetch(n)` so it does `await asyncio.sleep(0)` then "
        "returns `n * 2`. Then define the coroutine `double_all(nums)` that uses "
        "`asyncio.gather` to run `fetch` on every number concurrently and returns the "
        "results **in order**. Use the provided `run_async` helper to run it.\n"
        "\n"
        "**Examples**\n"
        "\n"
        "```\n"
        "run_async(double_all([1, 2, 3])) \u2192 [2, 4, 6]\n"
        "```"
    ),
    code(
        "# YOUR CODE\n"
        "import asyncio\n"
        "\n"
        "async def fetch(n):\n"
        "    pass\n"
        "\n"
        "async def double_all(nums):\n"
        "    pass\n"
    ),
    code(
        "check_equal('basic', run_async(double_all([1, 2, 3])), [2, 4, 6])\n"
        "check_equal('order', run_async(double_all([4, 0, 5])), [8, 0, 10])\n"
    ),

    md(
        "---\n"
        "\n"
        "## Problem 6: async timeout `Medium`\n"
        "\n"
        "Define the coroutine `guard(coro, limit)` that returns the awaited result of "
        "`coro` if it finishes within `limit` seconds, otherwise returns the string "
        "`'timeout'`. Use `asyncio.wait_for` and catch `asyncio.TimeoutError`.\n"
        "\n"
        "**Examples**\n"
        "\n"
        "```\n"
        "fast coroutine \u2192 its value;   slow coroutine \u2192 'timeout'\n"
        "```"
    ),
    code(
        "# YOUR CODE\n"
        "import asyncio\n"
        "\n"
        "async def guard(coro, limit):\n"
        "    pass\n"
    ),
    code(
        "async def quick():\n"
        "    await asyncio.sleep(0.01)\n"
        "    return 'done'\n"
        "\n"
        "async def slow():\n"
        "    await asyncio.sleep(1)\n"
        "    return 'done'\n"
        "\n"
        "check_equal('fast', run_async(guard(quick(), 0.5)), 'done')\n"
        "check_equal('slow', run_async(guard(slow(), 0.1)), 'timeout')\n"
    ),

    md(
        "---\n"
        "\n"
        "## Problem 7: choose the right tool `Easy`\n"
        "\n"
        "From the GIL and decision-guide lessons, define `best_tool(workload)` that "
        "returns the recommended approach as a string:\n"
        "\n"
        "- `'cpu'` (heavy computation) \u2192 `'multiprocessing'`\n"
        "- `'io_few'` (a handful of I/O waits) \u2192 `'threading'`\n"
        "- `'io_many'` (thousands of I/O waits) \u2192 `'asyncio'`\n"
        "\n"
        "**Examples**\n"
        "\n"
        "```\n"
        "best_tool('cpu') \u2192 'multiprocessing'\n"
        "```"
    ),
    code(
        "# YOUR CODE\n"
        "def best_tool(workload):\n"
        "    pass\n"
    ),
    code(
        "check_equal('cpu', best_tool('cpu'), 'multiprocessing')\n"
        "check_equal('io_few', best_tool('io_few'), 'threading')\n"
        "check_equal('io_many', best_tool('io_many'), 'asyncio')\n"
    ),
]

# ---------------------------------------------------------------------------
# Notebook 18: Unit Testing
# ---------------------------------------------------------------------------
TEST_HELPERS = HELPERS + '''

def run_suite(test_case_cls):
    """Run a unittest.TestCase subclass; return True if every test passed."""
    import unittest
    suite = unittest.TestLoader().loadTestsFromTestCase(test_case_cls)
    result = unittest.TextTestRunner(verbosity=0).run(suite)
    return result.wasSuccessful()
'''

nb18 = [
    md(
        "# Practice: Unit Testing\n"
        "\n"
        "Write your solutions in the **YOUR CODE** cells, then run **Validate** cells.\n"
        "\n"
        "We use the built-in `unittest` and `unittest.mock` so everything runs inside "
        "the notebook (no separate `pytest` process needed). The setup cell adds a "
        "`run_suite(...)` helper that runs a `TestCase` and reports whether it passed."
    ),
    code(TEST_HELPERS),

    md(
        "---\n"
        "\n"
        "## Problem 1: code under test `Easy`\n"
        "\n"
        "Implement `divide(a, b)` that returns `a / b`, but raises `ValueError` with "
        "the exact message `'cannot divide by zero'` when `b == 0`. The later problems "
        "test this function.\n"
        "\n"
        "**Examples**\n"
        "\n"
        "```\n"
        "divide(10, 2) \u2192 5.0;   divide(1, 0) \u2192 raises ValueError\n"
        "```"
    ),
    code(
        "# YOUR CODE\n"
        "def divide(a, b):\n"
        "    pass\n"
    ),
    code(
        "check_equal('basic', divide(10, 2), 5.0)\n"
        "try:\n"
        "    divide(1, 0)\n"
        "    print('\u2717 raises \u2014 no error was raised')\n"
        "except ValueError as e:\n"
        "    check_equal('raises', str(e), 'cannot divide by zero')\n"
    ),

    md(
        "---\n"
        "\n"
        "## Problem 2: assert that it raises `Medium`\n"
        "\n"
        "Define `assert_raises(fn, exc)` that returns `True` if calling `fn()` raises an "
        "exception of type `exc`, and `False` otherwise (no exception, or a different "
        "type). This is the idea behind `assertRaises` / `pytest.raises`.\n"
        "\n"
        "**Examples**\n"
        "\n"
        "```\n"
        "assert_raises(lambda: 1 / 0, ZeroDivisionError) \u2192 True\n"
        "assert_raises(lambda: 1 + 1, ZeroDivisionError) \u2192 False\n"
        "```"
    ),
    code(
        "# YOUR CODE\n"
        "def assert_raises(fn, exc):\n"
        "    pass\n"
    ),
    code(
        "check_equal('catches', assert_raises(lambda: 1 / 0, ZeroDivisionError), True)\n"
        "check_equal('no_raise', assert_raises(lambda: 1 + 1, ZeroDivisionError), False)\n"
        "check_equal('wrong_type', assert_raises(lambda: 1 / 0, ValueError), False)\n"
    ),

    md(
        "---\n"
        "\n"
        "## Problem 3: parametrized checks `Medium`\n"
        "\n"
        "Define `run_cases(func, cases)` where `cases` is a list of `(args, expected)` "
        "tuples (`args` is itself a tuple). Call `func(*args)` for each case and return "
        "the **count** of cases where the result equals `expected`. This mirrors "
        "`pytest.mark.parametrize`.\n"
        "\n"
        "**Examples**\n"
        "\n"
        "```\n"
        "run_cases(lambda x: x * 2, [((2,), 4), ((3,), 6)]) \u2192 2\n"
        "```"
    ),
    code(
        "# YOUR CODE\n"
        "def run_cases(func, cases):\n"
        "    pass\n"
    ),
    code(
        "check_equal('all_pass', run_cases(lambda x: x * 2, [((2,), 4), ((3,), 6)]), 2)\n"
        "check_equal('some_fail', run_cases(lambda x: x * 2, [((2,), 4), ((3,), 99)]), 1)\n"
        "check_equal('add', run_cases(lambda a, b: a + b, [((1, 2), 3), ((5, 5), 10)]), 2)\n"
    ),

    md(
        "---\n"
        "\n"
        "## Problem 4: a unittest TestCase `Medium`\n"
        "\n"
        "Write a `unittest.TestCase` named `TestDivide` that tests the `divide` function "
        "from Problem 1:\n"
        "\n"
        "- `test_normal`: use `self.assertEqual` to check `divide(10, 2) == 5.0`\n"
        "- `test_zero`: use `self.assertRaises(ValueError)` to check `divide(1, 0)`\n"
        "\n"
        "Then run it with `run_suite(TestDivide)`.\n"
        "\n"
        "**Examples**\n"
        "\n"
        "```\n"
        "run_suite(TestDivide) \u2192 True\n"
        "```"
    ),
    code(
        "# YOUR CODE\n"
        "import unittest\n"
        "\n"
        "class TestDivide(unittest.TestCase):\n"
        "    def test_normal(self):\n"
        "        pass\n"
        "\n"
        "    def test_zero(self):\n"
        "        pass\n"
    ),
    code(
        "check_equal('suite_passes', run_suite(TestDivide), True)\n"
        "test_methods = [m for m in dir(TestDivide) if m.startswith('test_')]\n"
        "check_equal('has_two_tests', len(test_methods), 2)\n"
    ),

    md(
        "---\n"
        "\n"
        "## Problem 5: mocking a dependency `Medium`\n"
        "\n"
        "Implement `get_username(client, user_id)` that calls `client.fetch(user_id)` "
        "and returns the `'name'` field of the dict it returns. Writing it to take "
        "`client` as an argument makes it easy to test with a `Mock`.\n"
        "\n"
        "**Examples**\n"
        "\n"
        "```\n"
        "client.fetch returns {'name': 'Asha'} \u2192 get_username(client, 7) == 'Asha'\n"
        "```"
    ),
    code(
        "# YOUR CODE\n"
        "def get_username(client, user_id):\n"
        "    pass\n"
    ),
    code(
        "from unittest.mock import Mock\n"
        "client = Mock()\n"
        "client.fetch.return_value = {'name': 'Asha', 'id': 7}\n"
        "check_equal('returns_name', get_username(client, 7), 'Asha')\n"
        "check_equal('called_with', client.fetch.call_args.args, (7,))\n"
    ),

    md(
        "---\n"
        "\n"
        "## Problem 6: patching with mock `Medium`\n"
        "\n"
        "Implement `is_weekend()` so it calls the helper `now()` (already defined) and "
        "returns `True` only on Saturday or Sunday. Hint: `weekday()` gives Monday=0 ... "
        "Sunday=6, so the weekend is `5` or `6`. Calling `now()` (instead of "
        "`datetime.now()` directly) lets the test **patch** the clock.\n"
        "\n"
        "**Examples**\n"
        "\n"
        "```\n"
        "patched to a Saturday \u2192 True;   patched to a Wednesday \u2192 False\n"
        "```"
    ),
    code(
        "# YOUR CODE\n"
        "from datetime import datetime\n"
        "\n"
        "def now():\n"
        "    return datetime.now()\n"
        "\n"
        "def is_weekend():\n"
        "    pass\n"
    ),
    code(
        "from unittest.mock import patch\n"
        "from datetime import datetime\n"
        "\n"
        "with patch('__main__.now', return_value=datetime(2024, 1, 6)):  # Saturday\n"
        "    check_equal('saturday', is_weekend(), True)\n"
        "with patch('__main__.now', return_value=datetime(2024, 1, 3)):  # Wednesday\n"
        "    check_equal('wednesday', is_weekend(), False)\n"
    ),
]

write_notebook("17_concurrency_and_async_practice.ipynb", nb17)
write_notebook("18_unit_testing_practice.ipynb", nb18)
print("done")
