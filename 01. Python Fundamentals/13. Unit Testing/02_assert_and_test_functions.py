# 02 — assert and hand-written test functions
# Run: python 02_assert_and_test_functions.py
#
# Before frameworks, you can already write real tests using assert.
# A test is just a function that asserts the expected result.

from sample_code import add, divide, apply_discount

# --- 1. assert: passes silently, raises AssertionError when false ---
assert add(1, 1) == 2
assert add(-1, 1) == 0
# assert add(1, 1) == 3   # Uncomment -> AssertionError

# --- 2. Group related checks into named test functions ---
def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-2, -3) == -5

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3

def test_apply_discount():
    assert apply_discount(1000, 10) == 900
    assert apply_discount(1000, 0) == 1000
    assert apply_discount(1000, 100) == 0

# --- 3. A tiny runner that reports pass/fail ---
def run(tests):
    passed = 0
    for test in tests:
        try:
            test()
            print(f"PASS  {test.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"FAIL  {test.__name__}: {e}")
    print(f"\n{passed}/{len(tests)} tests passed")

if __name__ == "__main__":
    run([test_add, test_divide, test_apply_discount])

# This is exactly what unittest and pytest do for you — automatically
# discovering test functions, running them, and reporting results.
