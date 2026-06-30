# 08 — Testing

Learn how to test Python code: start with plain `assert`, move to the built-in
`unittest`, then `pytest`, mocking, and coverage.

```bash
# from repo root
.venv\Scripts\activate
pip install pytest pytest-cov

cd "01. Python Fundamentals/07. Advanced Topics/08. Testing"
```

## Files

| Order | File | Topic | How to run |
|-------|------|-------|------------|
| — | `sample_code.py` | Code under test (imported by lessons) | — |
| 01 | `01_why_test.py` | Why test; manual checks vs automatic | `python 01_why_test.py` |
| 02 | `02_assert_and_test_functions.py` | `assert`, hand-written test runner | `python 02_assert_and_test_functions.py` |
| 03 | `03_unittest_basics.py` | `unittest.TestCase`, `test_*` methods | `python 03_unittest_basics.py` |
| 04 | `04_unittest_assertions.py` | `assertEqual`, `assertRaises`, etc. | `python 04_unittest_assertions.py` |
| 05 | `05_unittest_fixtures.py` | `setUp` / `tearDown` / `setUpClass` | `python 05_unittest_fixtures.py` |
| 06 | `06_unittest_exceptions.py` | Testing raised exceptions | `python 06_unittest_exceptions.py` |
| 07 | `07_pytest_basics.py` | pytest + plain `assert` | `pytest "07_pytest_basics.py" -v` |
| 08 | `08_pytest_fixtures.py` | `@pytest.fixture`, scope, teardown | `pytest "08_pytest_fixtures.py" -v` |
| 09 | `09_pytest_parametrize.py` | One test, many inputs | `pytest "09_pytest_parametrize.py" -v` |
| 10 | `10_pytest_exceptions_and_marks.py` | `raises`, `approx`, skip / xfail | `pytest "10_pytest_exceptions_and_marks.py" -v` |
| 11 | `11_mocking_basics.py` | `Mock`, `patch` (fake dependencies) | `python 11_mocking_basics.py` |
| 12 | `12_coverage_and_best_practices.py` | AAA pattern, coverage, checklist | `pytest --cov=sample_code "12_coverage_and_best_practices.py"` |

## Key ideas

- **`assert`** — the foundation: passes silently, raises `AssertionError` when false.
- **`unittest`** — built in, class-based, lots of `assert*` helpers and fixtures.
- **`pytest`** — third-party, less boilerplate (plain `assert`), powerful fixtures and `parametrize`.
- **Mocking** — replace network/time/random/db with controllable fakes.
- **Coverage** — measures how much code your tests run (a guide, not a guarantee).

## unittest vs pytest

| | unittest | pytest |
|--|----------|--------|
| Install | built in | `pip install pytest` |
| Style | classes + `self.assertEqual` | functions + plain `assert` |
| Fixtures | `setUp` / `tearDown` | `@pytest.fixture` (flexible scopes) |
| Many inputs | manual loops | `@pytest.mark.parametrize` |

**Tip:** real pytest projects name files `test_*.py` so they're auto-discovered.
These lessons use number prefixes for ordering, so run them by name (as above).
