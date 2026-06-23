"""One-time generator for practice notebooks. Run: python _generate_notebooks.py"""
import json
from pathlib import Path

OUT = Path(__file__).parent

HELPER_CELL = '''\
# Run this cell once per notebook — provides test validation helpers.

def check_equal(name, actual, expected):
    """Compare actual vs expected; print pass/fail."""
    if actual == expected:
        print(f"✓ {name}")
        return True
    print(f"✗ {name}")
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
            print(f"✗ {name} — Error: {type(exc).__name__}: {exc}")
    total = len(cases)
    print(f"\\nResult: {passed}/{total} passed")
    if passed == total:
        print("🎉 All tests passed!")
    return passed == total
'''

INTRO = """# How to use these practice notebooks

1. **Read** the problem in the markdown cell.
2. **Write your code** in the code cell marked `YOUR CODE`.
3. **Run** the validation cell below it to check your answer.
4. Fix your code until all tests show ✓.

**Tips**
- Do not edit the validation cells unless a problem says so.
- Run the helper cell at the top once when you open a notebook.
- Problems are ordered easy → harder within each topic.
- Matches lessons in `01`–`07` folders of Python Fundamentals.

| Notebook | Topic |
|----------|-------|
| 01 | Getting Started — print, variables, input, casting, f-strings |
| 02 | Operators & Types |
| 03 | Control Flow — if, loops |
| 04 | Strings |
| 05 | Lists |
| 06 | Tuples & Sets |
| 07 | Dictionaries |
| 08 | Functions |
| 09 | Comprehensions |
| 10 | OOP Basics |
| 11 | Exceptions |
"""


def md(text: str) -> dict:
    return {"cell_type": "markdown", "metadata": {}, "source": text.splitlines(keepends=True)}


def code(text: str) -> dict:
    return {
        "cell_type": "code",
        "metadata": {},
        "source": text.splitlines(keepends=True),
        "outputs": [],
        "execution_count": None,
    }


def notebook(title: str, problems: list[dict], include_helper: bool = True) -> dict:
    cells = [md(f"# {title}\n\nWrite your solutions in the **YOUR CODE** cells, then run **Validate** cells.\n")]
    if include_helper:
        cells.append(code(HELPER_CELL))
    for p in problems:
        diff = p.get("difficulty", "Easy")
        cells.append(
            md(
                f"---\n\n## Problem {p['id']}: {p['title']} `{diff}`\n\n"
                f"{p['description']}\n\n"
                f"**Examples**\n\n{p['examples']}\n"
            )
        )
        cells.append(code(p["stub"]))
        cells.append(code(p["validate"]))
    return {
        "nbformat": 4,
        "nbformat_minor": 5,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.11.0"},
        },
        "cells": cells,
    }


def save(name: str, nb: dict) -> None:
    path = OUT / name
    path.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"Created {path.name}")


NOTEBOOKS = {
    "00_how_to_use.ipynb": {
        "nbformat": 4,
        "nbformat_minor": 5,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.11.0"},
        },
        "cells": [md(INTRO)],
    },

    "01_getting_started_practice.ipynb": notebook(
        "Practice: Getting Started",
        [
            {
                "id": 1,
                "title": "Hello, Python!",
                "difficulty": "Easy",
                "description": "Store the exact message `Hello, Python!` in a variable called `message`.",
                "examples": "```\nmessage → \"Hello, Python!\"\n```",
                "stub": "# YOUR CODE\nmessage = None  # replace with your solution\n",
                "validate": 'check_equal("message", message, "Hello, Python!")\n',
            },
            {
                "id": 2,
                "title": "Greeting with f-string",
                "difficulty": "Easy",
                "description": "Given `name = \"Darshan\"`, build `greeting` so it equals `Hello, Darshan!` using an **f-string**.",
                "examples": '```\nname = "Darshan"\ngreeting → "Hello, Darshan!"\n```',
                "stub": 'name = "Darshan"\n\n# YOUR CODE\ngreeting = None\n',
                "validate": 'check_equal("greeting", greeting, "Hello, Darshan!")\n',
            },
            {
                "id": 3,
                "title": "Next year age",
                "difficulty": "Easy",
                "description": "Given `age = 25` (int), set `next_age` to age plus one **without** converting types.",
                "examples": "```\nage = 25\nnext_age → 26\n```",
                "stub": "age = 25\n\n# YOUR CODE\nnext_age = None\n",
                "validate": "check_equal('next_age', next_age, 26)\ncheck_equal('type is int', isinstance(next_age, int), True)\n",
            },
            {
                "id": 4,
                "title": "String to integer",
                "difficulty": "Easy",
                "description": "`score_text = \"95\"` simulates `input()`. Convert it to an int stored in `score`, then set `bonus` to `score + 5`.",
                "examples": '```\nscore_text = "95"\nscore → 95\nbonus → 100\n```',
                "stub": 'score_text = "95"\n\n# YOUR CODE\nscore = None\nbonus = None\n',
                "validate": "check_equal('score', score, 95)\ncheck_equal('bonus', bonus, 100)\n",
            },
            {
                "id": 5,
                "title": "Strip spaces",
                "difficulty": "Easy",
                "description": "Clean `raw_city` with `.strip()` and store the result in `city`.",
                "examples": '```\nraw_city = "  Mumbai  "\ncity → "Mumbai"\n```',
                "stub": 'raw_city = "  Mumbai  "\n\n# YOUR CODE\ncity = None\n',
                "validate": 'check_equal("city", city, "Mumbai")\n',
            },
            {
                "id": 6,
                "title": "Float formatting",
                "difficulty": "Easy",
                "description": "Given `pi = 3.14159265`, create `formatted` as the string `Pi is 3.14` using an f-string with **2 decimal places**.",
                "examples": '```\nformatted → "Pi is 3.14"\n```',
                "stub": "pi = 3.14159265\n\n# YOUR CODE\nformatted = None\n",
                "validate": 'check_equal("formatted", formatted, "Pi is 3.14")\n',
            },
            {
                "id": 7,
                "title": "Unpack three values",
                "difficulty": "Medium",
                "description": "Unpack `data` into three variables `day`, `month`, `year` in one line.",
                "examples": '```\ndata = ("Mon", 6, 2026)\nday → "Mon", month → 6, year → 2026\n```',
                "stub": 'data = ("Mon", 6, 2026)\n\n# YOUR CODE\nday = month = year = None\n',
                "validate": 'check_equal("day", day, "Mon")\ncheck_equal("month", month, 6)\ncheck_equal("year", year, 2026)\n',
            },
            {
                "id": 8,
                "title": "Truthy check",
                "difficulty": "Medium",
                "description": "Set `has_name` to `True` if `name` is non-empty after `.strip()`, else `False`. Test with the given value.",
                "examples": '```\nname = "  "\nhas_name → False\n```',
                "stub": 'name = "  "\n\n# YOUR CODE\nhas_name = None\n',
                "validate": "check_equal('has_name', has_name, False)\n",
            },
        ],
    ),

    "02_operators_and_types_practice.ipynb": notebook(
        "Practice: Operators & Types",
        [
            {
                "id": 1,
                "title": "Sum and product",
                "difficulty": "Easy",
                "description": "Given `a = 12` and `b = 5`, set `total` to their sum and `product` to their product.",
                "examples": "```\ntotal → 17, product → 60\n```",
                "stub": "a, b = 12, 5\n\n# YOUR CODE\ntotal = product = None\n",
                "validate": "check_equal('total', total, 17)\ncheck_equal('product', product, 60)\n",
            },
            {
                "id": 2,
                "title": "Floor division and remainder",
                "difficulty": "Easy",
                "description": "For `n = 17` and `d = 5`, compute `quotient` with `//` and `remainder` with `%`.",
                "examples": "```\nquotient → 3, remainder → 2\n```",
                "stub": "n, d = 17, 5\n\n# YOUR CODE\nquotient = remainder = None\n",
                "validate": "check_equal('quotient', quotient, 3)\ncheck_equal('remainder', remainder, 2)\n",
            },
            {
                "id": 3,
                "title": "Power",
                "difficulty": "Easy",
                "description": "Set `result` to `2` raised to the power `10` using `**`.",
                "examples": "```\nresult → 1024\n```",
                "stub": "# YOUR CODE\nresult = None\n",
                "validate": "check_equal('result', result, 1024)\n",
            },
            {
                "id": 4,
                "title": "String repeat",
                "difficulty": "Easy",
                "description": 'Build `line` equal to `"ha"` repeated 3 times → `"hahaha"`.',
                "examples": '```\nline → "hahaha"\n```',
                "stub": "# YOUR CODE\nline = None\n",
                "validate": 'check_equal("line", line, "hahaha")\n',
            },
            {
                "id": 5,
                "title": "Comparisons",
                "difficulty": "Easy",
                "description": "Given `x = 10` and `y = 20`, set `is_less`, `is_equal`, `is_not_equal` to the correct boolean results.",
                "examples": "```\nis_less → True, is_equal → False, is_not_equal → True\n```",
                "stub": "x, y = 10, 20\n\n# YOUR CODE\nis_less = is_equal = is_not_equal = None\n",
                "validate": "check_equal('is_less', is_less, True)\ncheck_equal('is_equal', is_equal, False)\ncheck_equal('is_not_equal', is_not_equal, True)\n",
            },
            {
                "id": 6,
                "title": "Logical combo",
                "difficulty": "Easy",
                "description": "`can_vote` is True when `age >= 18` **and** `has_id` is True. Use the given values.",
                "examples": "```\nage = 20, has_id = True → can_vote = True\n```",
                "stub": "age = 20\nhas_id = True\n\n# YOUR CODE\ncan_vote = None\n",
                "validate": "check_equal('can_vote', can_vote, True)\n",
            },
            {
                "id": 7,
                "title": "Float to int truncate",
                "difficulty": "Medium",
                "description": "Convert `value = 9.99` to int using `int()` (truncates). Store in `whole`.",
                "examples": "```\nwhole → 9\n```",
                "stub": "value = 9.99\n\n# YOUR CODE\nwhole = None\n",
                "validate": "check_equal('whole', whole, 9)\n",
            },
            {
                "id": 8,
                "title": "Operator precedence",
                "difficulty": "Medium",
                "description": "Evaluate `2 + 3 * 4 ** 2` and store in `answer` (should be 50, not 80 or 144).",
                "examples": "```\nanswer → 50\n```",
                "stub": "# YOUR CODE\nanswer = None\n",
                "validate": "check_equal('answer', answer, 50)\n",
            },
        ],
    ),

    "03_control_flow_practice.ipynb": notebook(
        "Practice: Control Flow",
        [
            {
                "id": 1,
                "title": "Pass or fail",
                "difficulty": "Easy",
                "description": "Set `status` to `\"Pass\"` if `marks >= 40`, else `\"Fail\"`. Given `marks = 55`.",
                "examples": '```\nstatus → "Pass"\n```',
                "stub": "marks = 55\n\n# YOUR CODE\nstatus = None\n",
                "validate": 'check_equal("status", status, "Pass")\n',
            },
            {
                "id": 2,
                "title": "Grade letter",
                "difficulty": "Medium",
                "description": "Map `score` to a letter: 90+ → `A`, 75+ → `B`, 60+ → `C`, else `F`. Given `score = 82`.",
                "examples": '```\nscore = 82 → letter = "B"\n```',
                "stub": "score = 82\n\n# YOUR CODE\nletter = None\n",
                "validate": 'check_equal("letter", letter, "B")\n',
            },
            {
                "id": 3,
                "title": "Sum 1 to n",
                "difficulty": "Easy",
                "description": "Use a `for` loop to sum integers from 1 to `n` inclusive. Given `n = 10`.",
                "examples": "```\nn = 10 → total = 55\n```",
                "stub": "n = 10\n\n# YOUR CODE\ntotal = None\n",
                "validate": "check_equal('total', total, 55)\n",
            },
            {
                "id": 4,
                "title": "Count evens",
                "difficulty": "Easy",
                "description": "Count how many numbers in `nums` are even. Store in `even_count`.",
                "examples": "```\nnums = [1, 2, 3, 4, 6] → even_count = 3\n```",
                "stub": "nums = [1, 2, 3, 4, 6]\n\n# YOUR CODE\neven_count = None\n",
                "validate": "check_equal('even_count', even_count, 3)\n",
            },
            {
                "id": 5,
                "title": "While countdown list",
                "difficulty": "Medium",
                "description": "Use a `while` loop to build `countdown` as `[3, 2, 1]` starting from `start = 3`.",
                "examples": "```\ncountdown → [3, 2, 1]\n```",
                "stub": "start = 3\n\n# YOUR CODE\ncountdown = None\n",
                "validate": "check_equal('countdown', countdown, [3, 2, 1])\n",
            },
            {
                "id": 6,
                "title": "First greater than 10",
                "difficulty": "Medium",
                "description": "Loop through `nums` and set `first_big` to the **first** value > 10, or `None` if none.",
                "examples": "```\nnums = [3, 8, 11, 15] → first_big = 11\n```",
                "stub": "nums = [3, 8, 11, 15]\n\n# YOUR CODE\nfirst_big = None\n",
                "validate": "check_equal('first_big', first_big, 11)\n",
            },
            {
                "id": 7,
                "title": "Skip multiples of 3",
                "difficulty": "Medium",
                "description": "Build `result` with numbers 1–10 **excluding** multiples of 3. Use `continue`.",
                "examples": "```\nresult → [1, 2, 4, 5, 7, 8, 10]\n```",
                "stub": "# YOUR CODE\nresult = None\n",
                "validate": "check_equal('result', result, [1, 2, 4, 5, 7, 8, 10])\n",
            },
            {
                "id": 8,
                "title": "Multiplication row",
                "difficulty": "Medium",
                "description": "For `table = 5`, build `row` as `[5, 10, 15, 20, 25]` using a loop (5 × 1 … 5 × 5).",
                "examples": "```\ntable = 5 → row = [5, 10, 15, 20, 25]\n```",
                "stub": "table = 5\n\n# YOUR CODE\nrow = None\n",
                "validate": "check_equal('row', row, [5, 10, 15, 20, 25])\n",
            },
            {
                "id": 9,
                "title": "Fizz value",
                "difficulty": "Easy",
                "description": "Classic mini-Fizz: for `n = 9`, set `label` to `\"Fizz\"` if divisible by 3, else str(n).",
                "examples": '```\nn = 9 → label = "Fizz"\n```',
                "stub": "n = 9\n\n# YOUR CODE\nlabel = None\n",
                "validate": 'check_equal("label", label, "Fizz")\n',
            },
            {
                "id": 10,
                "title": "Nested loop — pairs",
                "difficulty": "Hard",
                "description": "Build `pairs`: all `(i, j)` where `i` in 1..2 and `j` in 1..3 as tuples in a list.",
                "examples": "```\npairs → [(1,1), (1,2), (1,3), (2,1), (2,2), (2,3)]\n```",
                "stub": "# YOUR CODE\npairs = None\n",
                "validate": "check_equal('pairs', pairs, [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3)])\n",
            },
        ],
    ),

    "04_strings_practice.ipynb": notebook(
        "Practice: Strings",
        [
            {
                "id": 1,
                "title": "Reverse a string",
                "difficulty": "Easy",
                "description": "Reverse `text` using slicing and store in `reversed_text`.",
                "examples": '```\ntext = "Python" → reversed_text = "nohtyP"\n```',
                "stub": 'text = "Python"\n\n# YOUR CODE\nreversed_text = None\n',
                "validate": 'check_equal("reversed_text", reversed_text, "nohtyP")\n',
            },
            {
                "id": 2,
                "title": "Count vowels",
                "difficulty": "Easy",
                "description": "Count vowels `aeiou` (lowercase) in `word`. Given `word = \"education\"`.",
                "examples": '```\nvowel_count → 5\n```',
                "stub": 'word = "education"\n\n# YOUR CODE\nvowel_count = None\n',
                "validate": "check_equal('vowel_count', vowel_count, 5)\n",
            },
            {
                "id": 3,
                "title": "Title case word",
                "difficulty": "Easy",
                "description": "Turn `name = \"darshan\"` into `\"Darshan\"` using string methods.",
                "examples": '```\nproper → "Darshan"\n```',
                "stub": 'name = "darshan"\n\n# YOUR CODE\nproper = None\n',
                "validate": 'check_equal("proper", proper, "Darshan")\n',
            },
            {
                "id": 4,
                "title": "Palindrome check",
                "difficulty": "Medium",
                "description": "Set `is_palindrome` to True if `s` reads the same forwards and backwards. `s = \"level\"`.",
                "examples": "```\nis_palindrome → True\n```",
                "stub": 's = "level"\n\n# YOUR CODE\nis_palindrome = None\n',
                "validate": "check_equal('is_palindrome', is_palindrome, True)\n",
            },
            {
                "id": 5,
                "title": "Replace word",
                "difficulty": "Easy",
                "description": 'Replace `"bad"` with `"good"` in `sentence`.',
                "examples": '```\n"bad day" → "good day"\n```',
                "stub": 'sentence = "bad day"\n\n# YOUR CODE\nfixed = None\n',
                "validate": 'check_equal("fixed", fixed, "good day")\n',
            },
            {
                "id": 6,
                "title": "Split and join",
                "difficulty": "Medium",
                "description": 'Split `csv` by commas, then join with `" | "` → `"a | b | c"`.',
                "examples": '```\ncsv = "a,b,c"\n```',
                "stub": 'csv = "a,b,c"\n\n# YOUR CODE\njoined = None\n',
                "validate": 'check_equal("joined", joined, "a | b | c")\n',
            },
            {
                "id": 7,
                "title": "First three chars",
                "difficulty": "Easy",
                "description": "Slice the first 3 characters of `lang` into `short`.",
                "examples": '```\nlang = "Python" → short = "Pyt"\n```',
                "stub": 'lang = "Python"\n\n# YOUR CODE\nshort = None\n',
                "validate": 'check_equal("short", short, "Pyt")\n',
            },
            {
                "id": 8,
                "title": "Case-insensitive compare",
                "difficulty": "Medium",
                "description": "Set `same` to True if `a` and `b` are equal ignoring case and outer spaces.",
                "examples": '```\na = "  Hello ", b = "hello" → same = True\n```',
                "stub": 'a = "  Hello "\nb = "hello"\n\n# YOUR CODE\nsame = None\n',
                "validate": "check_equal('same', same, True)\n",
            },
        ],
    ),

    "05_lists_practice.ipynb": notebook(
        "Practice: Lists",
        [
            {
                "id": 1,
                "title": "List sum",
                "difficulty": "Easy",
                "description": "Sum all numbers in `nums` using a loop (not `sum()`).",
                "examples": "```\nnums = [4, 5, 6] → total = 15\n```",
                "stub": "nums = [4, 5, 6]\n\n# YOUR CODE\ntotal = None\n",
                "validate": "check_equal('total', total, 15)\n",
            },
            {
                "id": 2,
                "title": "Find maximum",
                "difficulty": "Medium",
                "description": "Find the largest value in `nums` without using `max()`.",
                "examples": "```\nnums = [3, 9, 1, 7] → biggest = 9\n```",
                "stub": "nums = [3, 9, 1, 7]\n\n# YOUR CODE\nbiggest = None\n",
                "validate": "check_equal('biggest', biggest, 9)\n",
            },
            {
                "id": 3,
                "title": "Reverse list",
                "difficulty": "Easy",
                "description": "Reverse `items` into a **new** list `rev` (do not mutate `items`).",
                "examples": "```\nitems = [1, 2, 3] → rev = [3, 2, 1]\n```",
                "stub": "items = [1, 2, 3]\n\n# YOUR CODE\nrev = None\n",
                "validate": "check_equal('rev', rev, [3, 2, 1])\ncheck_equal('items unchanged', items, [1, 2, 3])\n",
            },
            {
                "id": 4,
                "title": "Unique preserving order",
                "difficulty": "Medium",
                "description": "Build `unique` with duplicates removed, keeping first occurrence order.",
                "examples": "```\n[1, 2, 2, 3, 1] → [1, 2, 3]\n```",
                "stub": "nums = [1, 2, 2, 3, 1]\n\n# YOUR CODE\nunique = None\n",
                "validate": "check_equal('unique', unique, [1, 2, 3])\n",
            },
            {
                "id": 5,
                "title": "Second largest",
                "difficulty": "Medium",
                "description": "Return the second largest value in `nums` (assume at least 2 distinct values).",
                "examples": "```\nnums = [10, 5, 8, 20, 15] → second = 15\n```",
                "stub": "nums = [10, 5, 8, 20, 15]\n\n# YOUR CODE\nsecond = None\n",
                "validate": "check_equal('second', second, 15)\n",
            },
            {
                "id": 6,
                "title": "Append squares",
                "difficulty": "Easy",
                "description": "Start with `squares = []` and append squares of 1..5 using a loop.",
                "examples": "```\nsquares → [1, 4, 9, 16, 25]\n```",
                "stub": "# YOUR CODE\nsquares = None\n",
                "validate": "check_equal('squares', squares, [1, 4, 9, 16, 25])\n",
            },
            {
                "id": 7,
                "title": "Count occurrences",
                "difficulty": "Easy",
                "description": "Count how many times `target` appears in `items`.",
                "examples": '```\nitems = ["a", "b", "a", "c"], target = "a" → count = 2\n```',
                "stub": 'items = ["a", "b", "a", "c"]\ntarget = "a"\n\n# YOUR CODE\ncount = None\n',
                "validate": "check_equal('count', count, 2)\n",
            },
            {
                "id": 8,
                "title": "Rotate right by 1",
                "difficulty": "Hard",
                "description": "Rotate `nums` right by 1: last element moves to front. New list in `rotated`.",
                "examples": "```\n[1, 2, 3, 4] → [4, 1, 2, 3]\n```",
                "stub": "nums = [1, 2, 3, 4]\n\n# YOUR CODE\nrotated = None\n",
                "validate": "check_equal('rotated', rotated, [4, 1, 2, 3])\n",
            },
            {
                "id": 9,
                "title": "Filter positives",
                "difficulty": "Medium",
                "description": "Build `positives` with only values > 0 from `mixed`.",
                "examples": "```\n[-1, 2, 0, 5, -3] → [2, 5]\n```",
                "stub": "mixed = [-1, 2, 0, 5, -3]\n\n# YOUR CODE\npositives = None\n",
                "validate": "check_equal('positives', positives, [2, 5])\n",
            },
            {
                "id": 10,
                "title": "Merge lists",
                "difficulty": "Easy",
                "description": "Combine `a` and `b` into `combined` (concatenation).",
                "examples": "```\na = [1, 2], b = [3, 4] → [1, 2, 3, 4]\n```",
                "stub": "a, b = [1, 2], [3, 4]\n\n# YOUR CODE\ncombined = None\n",
                "validate": "check_equal('combined', combined, [1, 2, 3, 4])\n",
            },
        ],
    ),

    "06_tuples_and_sets_practice.ipynb": notebook(
        "Practice: Tuples & Sets",
        [
            {
                "id": 1,
                "title": "Swap with tuple unpacking",
                "difficulty": "Easy",
                "description": "Swap `x` and `y` in one line using tuple unpacking.",
                "examples": "```\nx=1, y=2 → x=2, y=1\n```",
                "stub": "x, y = 1, 2\n\n# YOUR CODE\n# swap x and y here\n",
                "validate": "check_equal('x', x, 2)\ncheck_equal('y', y, 1)\n",
            },
            {
                "id": 2,
                "title": "Tuple from range",
                "difficulty": "Easy",
                "description": "Create `t` as a tuple of numbers 0 through 4 using `range` and `tuple()`.",
                "examples": "```\nt → (0, 1, 2, 3, 4)\n```",
                "stub": "# YOUR CODE\nt = None\n",
                "validate": "check_equal('t', t, (0, 1, 2, 3, 4))\n",
            },
            {
                "id": 3,
                "title": "Set union",
                "difficulty": "Easy",
                "description": "Compute union of `a` and `b` into `all_tags` (unique, unordered). Compare as sets.",
                "examples": '```\na = {"py", "code"}, b = {"code", "ai"} → 3 unique tags\n```',
                "stub": 'a = {"py", "code"}\nb = {"code", "ai"}\n\n# YOUR CODE\nall_tags = None\n',
                "validate": 'check_equal("all_tags", all_tags, {"py", "code", "ai"})\n',
            },
            {
                "id": 4,
                "title": "Set intersection",
                "difficulty": "Easy",
                "description": "Find elements in both `a` and `b`, store as `common`.",
                "examples": "```\na = {1, 2, 3}, b = {3, 4} → {3}\n```",
                "stub": "a, b = {1, 2, 3}, {3, 4}\n\n# YOUR CODE\ncommon = None\n",
                "validate": "check_equal('common', common, {3})\n",
            },
            {
                "id": 5,
                "title": "Unique letters",
                "difficulty": "Medium",
                "description": "Build `letters` as a set of unique lowercase letters in `word`.",
                "examples": '```\nword = "hello" → {"h", "e", "l", "o"}\n```',
                "stub": 'word = "hello"\n\n# YOUR CODE\nletters = None\n',
                "validate": 'check_equal("letters", letters, {"h", "e", "l", "o"})\n',
            },
            {
                "id": 6,
                "title": "Remove duplicates with set",
                "difficulty": "Medium",
                "description": "Use a set to count distinct values in `nums`, store count in `distinct_count`.",
                "examples": "```\n[1, 2, 2, 3, 3, 3] → distinct_count = 3\n```",
                "stub": "nums = [1, 2, 2, 3, 3, 3]\n\n# YOUR CODE\ndistinct_count = None\n",
                "validate": "check_equal('distinct_count', distinct_count, 3)\n",
            },
        ],
    ),

    "07_dictionaries_practice.ipynb": notebook(
        "Practice: Dictionaries",
        [
            {
                "id": 1,
                "title": "Build a phone book entry",
                "difficulty": "Easy",
                "description": "Create `contact` dict with keys `\"name\"` and `\"phone\"` for Darshan / 9876543210.",
                "examples": '```\n{"name": "Darshan", "phone": 9876543210}\n```',
                "stub": "# YOUR CODE\ncontact = None\n",
                "validate": 'check_equal("contact", contact, {"name": "Darshan", "phone": 9876543210})\n',
            },
            {
                "id": 2,
                "title": "Safe get with default",
                "difficulty": "Easy",
                "description": "Read `scores[\"Bob\"]` with default `0` into `bob_score`.",
                "examples": '```\nscores = {"Alice": 90} → bob_score = 0\n```',
                "stub": 'scores = {"Alice": 90}\n\n# YOUR CODE\nbob_score = None\n',
                "validate": "check_equal('bob_score', bob_score, 0)\n",
            },
            {
                "id": 3,
                "title": "Word frequency",
                "difficulty": "Medium",
                "description": "Count each word in `words` into dict `freq`.",
                "examples": '```\n["a", "b", "a"] → {"a": 2, "b": 1}\n```',
                "stub": 'words = ["a", "b", "a"]\n\n# YOUR CODE\nfreq = None\n',
                "validate": 'check_equal("freq", freq, {"a": 2, "b": 1})\n',
            },
            {
                "id": 4,
                "title": "Merge dicts",
                "difficulty": "Easy",
                "description": "Merge `d1` and `d2` into `merged` (`d2` wins on duplicate keys).",
                "examples": '```\nd1 = {"x": 1}, d2 = {"y": 2, "x": 9} → {"x": 9, "y": 2}\n```',
                "stub": 'd1 = {"x": 1}\nd2 = {"y": 2, "x": 9}\n\n# YOUR CODE\nmerged = None\n',
                "validate": 'check_equal("merged", merged, {"x": 9, "y": 2})\n',
            },
            {
                "id": 5,
                "title": "Keys sorted",
                "difficulty": "Easy",
                "description": "Get sorted list of keys from `data` into `sorted_keys`.",
                "examples": '```\n{"z": 1, "a": 2} → ["a", "z"]\n```',
                "stub": 'data = {"z": 1, "a": 2}\n\n# YOUR CODE\nsorted_keys = None\n',
                "validate": 'check_equal("sorted_keys", sorted_keys, ["a", "z"])\n',
            },
            {
                "id": 6,
                "title": "Invert dict",
                "difficulty": "Medium",
                "description": "Swap keys and values of `original` into `inverted` (values are unique).",
                "examples": '```\n{"a": 1, "b": 2} → {1: "a", 2: "b"}\n```',
                "stub": 'original = {"a": 1, "b": 2}\n\n# YOUR CODE\ninverted = None\n',
                "validate": 'check_equal("inverted", inverted, {1: "a", 2: "b"})\n',
            },
            {
                "id": 7,
                "title": "Filter by value",
                "difficulty": "Medium",
                "description": "Build `passed` with only students whose score >= 40.",
                "examples": '```\n{"A": 55, "B": 30, "C": 40} → {"A": 55, "C": 40}\n```',
                "stub": 'grades = {"A": 55, "B": 30, "C": 40}\n\n# YOUR CODE\npassed = None\n',
                "validate": 'check_equal("passed", passed, {"A": 55, "C": 40})\n',
            },
            {
                "id": 8,
                "title": "Nested access",
                "difficulty": "Easy",
                "description": "Read city from nested dict into `city`.",
                "examples": '```\nuser["address"]["city"] → "Mumbai"\n```',
                "stub": 'user = {"name": "D", "address": {"city": "Mumbai", "zip": 400001}}\n\n# YOUR CODE\ncity = None\n',
                "validate": 'check_equal("city", city, "Mumbai")\n',
            },
        ],
    ),

    "08_functions_practice.ipynb": notebook(
        "Practice: Functions",
        [
            {
                "id": 1,
                "title": "greet",
                "difficulty": "Easy",
                "description": "Define `greet(name)` returning `f\"Hello, {name}!\"`.",
                "examples": '```\ngreet("Ada") → "Hello, Ada!"\n```',
                "stub": "# YOUR CODE\ndef greet(name):\n    pass\n",
                "validate": 'check_equal(\'greet("Ada")\', greet("Ada"), "Hello, Ada!")\n',
            },
            {
                "id": 2,
                "title": "is_even",
                "difficulty": "Easy",
                "description": "Define `is_even(n)` returning True if n is divisible by 2.",
                "examples": "```\nis_even(4) → True, is_even(7) → False\n```",
                "stub": "# YOUR CODE\ndef is_even(n):\n    pass\n",
                "validate": "check_equal('is_even(4)', is_even(4), True)\ncheck_equal('is_even(7)', is_even(7), False)\n",
            },
            {
                "id": 3,
                "title": "rectangle_area",
                "difficulty": "Easy",
                "description": "Define `rectangle_area(w, h)` returning width × height.",
                "examples": "```\nrectangle_area(3, 4) → 12\n```",
                "stub": "# YOUR CODE\ndef rectangle_area(w, h):\n    pass\n",
                "validate": "check_equal('area', rectangle_area(3, 4), 12)\n",
            },
            {
                "id": 4,
                "title": "max_of_three",
                "difficulty": "Medium",
                "description": "Define `max_of_three(a, b, c)` without using built-in `max()`.",
                "examples": "```\nmax_of_three(1, 9, 3) → 9\n```",
                "stub": "# YOUR CODE\ndef max_of_three(a, b, c):\n    pass\n",
                "validate": "check_equal('max', max_of_three(1, 9, 3), 9)\n",
            },
            {
                "id": 5,
                "title": "sum_all (*args)",
                "difficulty": "Medium",
                "description": "Define `sum_all(*args)` returning the sum of all numeric arguments.",
                "examples": "```\nsum_all(1, 2, 3) → 6\n```",
                "stub": "# YOUR CODE\ndef sum_all(*args):\n    pass\n",
                "validate": "check_equal('sum_all', sum_all(1, 2, 3), 6)\ncheck_equal('sum_all one', sum_all(10), 10)\n",
            },
            {
                "id": 6,
                "title": "power with default",
                "difficulty": "Medium",
                "description": "Define `power(base, exp=2)` — default exponent is 2.",
                "examples": "```\npower(5) → 25, power(2, 3) → 8\n```",
                "stub": "# YOUR CODE\ndef power(base, exp=2):\n    pass\n",
                "validate": "check_equal('power(5)', power(5), 25)\ncheck_equal('power(2,3)', power(2, 3), 8)\n",
            },
            {
                "id": 7,
                "title": "min_max",
                "difficulty": "Medium",
                "description": "Define `min_max(nums)` returning a tuple `(smallest, largest)`.",
                "examples": "```\nmin_max([3, 1, 4]) → (1, 4)\n```",
                "stub": "# YOUR CODE\ndef min_max(nums):\n    pass\n",
                "validate": "check_equal('min_max', min_max([3, 1, 4]), (1, 4))\n",
            },
            {
                "id": 8,
                "title": "factorial",
                "difficulty": "Medium",
                "description": "Define `factorial(n)` for n >= 0 using a loop.",
                "examples": "```\nfactorial(5) → 120, factorial(0) → 1\n```",
                "stub": "# YOUR CODE\ndef factorial(n):\n    pass\n",
                "validate": "check_equal('factorial(5)', factorial(5), 120)\ncheck_equal('factorial(0)', factorial(0), 1)\n",
            },
            {
                "id": 9,
                "title": "count_vowels function",
                "difficulty": "Medium",
                "description": "Define `count_vowels(text)` returning vowel count (aeiou, case-insensitive).",
                "examples": '```\ncount_vowels("Hello") → 2\n```',
                "stub": "# YOUR CODE\ndef count_vowels(text):\n    pass\n",
                "validate": 'check_equal("count_vowels", count_vowels("Hello"), 2)\n',
            },
            {
                "id": 10,
                "title": "apply_twice",
                "difficulty": "Hard",
                "description": "Define `apply_twice(f, x)` that returns `f(f(x))`.",
                "examples": "```\napply_twice(lambda n: n + 1, 3) → 5\n```",
                "stub": "# YOUR CODE\ndef apply_twice(f, x):\n    pass\n",
                "validate": "check_equal('apply_twice', apply_twice(lambda n: n + 1, 3), 5)\n",
            },
        ],
    ),

    "09_comprehensions_practice.ipynb": notebook(
        "Practice: Comprehensions",
        [
            {
                "id": 1,
                "title": "Squares list comprehension",
                "difficulty": "Easy",
                "description": "Build `squares` = squares of 1..5 using a list comprehension.",
                "examples": "```\n[1, 4, 9, 16, 25]\n```",
                "stub": "# YOUR CODE\nsquares = None\n",
                "validate": "check_equal('squares', squares, [1, 4, 9, 16, 25])\n",
            },
            {
                "id": 2,
                "title": "Evens only",
                "difficulty": "Easy",
                "description": "List comprehension: even numbers from 1..10 into `evens`.",
                "examples": "```\n[2, 4, 6, 8, 10]\n```",
                "stub": "# YOUR CODE\nevens = None\n",
                "validate": "check_equal('evens', evens, [2, 4, 6, 8, 10])\n",
            },
            {
                "id": 3,
                "title": "Uppercase names",
                "difficulty": "Easy",
                "description": "Uppercase each name in `names` using a list comprehension.",
                "examples": '```\n["ada", "guido"] → ["ADA", "GUIDO"]\n```',
                "stub": 'names = ["ada", "guido"]\n\n# YOUR CODE\nupper = None\n',
                "validate": 'check_equal("upper", upper, ["ADA", "GUIDO"])\n',
            },
            {
                "id": 4,
                "title": "Dict from pairs",
                "difficulty": "Medium",
                "description": "Build `scores` dict from parallel lists `students` and `marks` using dict comprehension or zip.",
                "examples": '```\nstudents = ["A", "B"], marks = [90, 85]\n```',
                "stub": 'students = ["A", "B"]\nmarks = [90, 85]\n\n# YOUR CODE\nscores = None\n',
                "validate": 'check_equal("scores", scores, {"A": 90, "B": 85})\n',
            },
            {
                "id": 5,
                "title": "Set of lengths",
                "difficulty": "Medium",
                "description": "Set comprehension: unique word lengths from `words`.",
                "examples": '```\n["hi", "hey", "yo"] → {2, 3}\n```',
                "stub": 'words = ["hi", "hey", "yo"]\n\n# YOUR CODE\nlengths = None\n',
                "validate": "check_equal('lengths', lengths, {2, 3})\n",
            },
            {
                "id": 6,
                "title": "Flatten matrix",
                "difficulty": "Hard",
                "description": "Use nested list comprehension to flatten `matrix` into `flat`.",
                "examples": "```\n[[1, 2], [3]] → [1, 2, 3]\n```",
                "stub": "matrix = [[1, 2], [3]]\n\n# YOUR CODE\nflat = None\n",
                "validate": "check_equal('flat', flat, [1, 2, 3])\n",
            },
        ],
    ),

    "10_oop_basics_practice.ipynb": notebook(
        "Practice: OOP Basics",
        [
            {
                "id": 1,
                "title": "Simple Dog class",
                "difficulty": "Easy",
                "description": "Define class `Dog` with `__init__(self, name)` setting `self.name`. Method `speak()` returns `f\"{self.name} says woof!\"`.",
                "examples": '```\nDog("Rex").speak() → "Rex says woof!"\n```',
                "stub": "# YOUR CODE\nclass Dog:\n    pass\n",
                "validate": 'check_equal("speak", Dog("Rex").speak(), "Rex says woof!")\n',
            },
            {
                "id": 2,
                "title": "Rectangle attributes",
                "difficulty": "Easy",
                "description": "Class `Rectangle` with `width`, `height` in `__init__`. Method `area()` returns width × height.",
                "examples": "```\nRectangle(3, 4).area() → 12\n```",
                "stub": "# YOUR CODE\nclass Rectangle:\n    pass\n",
                "validate": "check_equal('area', Rectangle(3, 4).area(), 12)\n",
            },
            {
                "id": 3,
                "title": "BankAccount deposit",
                "difficulty": "Medium",
                "description": "Class `BankAccount` starts with `balance=0`. Method `deposit(amount)` adds to balance and returns new balance.",
                "examples": "```\nacc = BankAccount(); acc.deposit(100) → 100\n```",
                "stub": "# YOUR CODE\nclass BankAccount:\n    pass\n",
                "validate": "acc = BankAccount()\ncheck_equal('deposit', acc.deposit(100), 100)\ncheck_equal('balance', acc.balance, 100)\n",
            },
            {
                "id": 4,
                "title": "Person full_name",
                "difficulty": "Easy",
                "description": "Class `Person` with `first` and `last`. Method `full_name()` returns `\"first last\"`.",
                "examples": '```\nPerson("Ada", "Lovelace").full_name() → "Ada Lovelace"\n```',
                "stub": "# YOUR CODE\nclass Person:\n    pass\n",
                "validate": 'check_equal("full", Person("Ada", "Lovelace").full_name(), "Ada Lovelace")\n',
            },
            {
                "id": 5,
                "title": "Counter increment",
                "difficulty": "Medium",
                "description": "Class `Counter` with `count=0`. Methods `increment()` (+1) and `reset()` (back to 0).",
                "examples": "```\nc = Counter(); c.increment(); c.increment(); c.count → 2\n```",
                "stub": "# YOUR CODE\nclass Counter:\n    pass\n",
                "validate": "c = Counter()\nc.increment()\nc.increment()\ncheck_equal('count', c.count, 2)\nc.reset()\ncheck_equal('after reset', c.count, 0)\n",
            },
            {
                "id": 6,
                "title": "Inheritance — Animal/Cat",
                "difficulty": "Medium",
                "description": "`Animal` has `name`. `Cat` inherits `Animal`, `sound()` returns `f\"{self.name} says meow\"`.",
                "examples": '```\nCat("Luna").sound() → "Luna says meow"\n```',
                "stub": "# YOUR CODE\nclass Animal:\n    pass\n\nclass Cat(Animal):\n    pass\n",
                "validate": 'check_equal("sound", Cat("Luna").sound(), "Luna says meow")\n',
            },
        ],
    ),

    "11_exceptions_practice.ipynb": notebook(
        "Practice: Exceptions",
        [
            {
                "id": 1,
                "title": "safe_int",
                "difficulty": "Easy",
                "description": "Define `safe_int(text)` — return `int(text)` or `None` if `ValueError`.",
                "examples": '```\nsafe_int("42") → 42, safe_int("x") → None\n```',
                "stub": "# YOUR CODE\ndef safe_int(text):\n    pass\n",
                "validate": "check_equal('valid', safe_int('42'), 42)\ncheck_equal('invalid', safe_int('x'), None)\n",
            },
            {
                "id": 2,
                "title": "safe_divide",
                "difficulty": "Easy",
                "description": "Define `safe_divide(a, b)` — return `a/b` or `None` on `ZeroDivisionError`.",
                "examples": "```\nsafe_divide(10, 2) → 5.0, safe_divide(1, 0) → None\n```",
                "stub": "# YOUR CODE\ndef safe_divide(a, b):\n    pass\n",
                "validate": "check_equal('ok', safe_divide(10, 2), 5.0)\ncheck_equal('zero', safe_divide(1, 0), None)\n",
            },
            {
                "id": 3,
                "title": "get_item",
                "difficulty": "Medium",
                "description": "Define `get_item(items, index)` — return `items[index]` or `None` on `IndexError`.",
                "examples": "```\nget_item([1,2], 1) → 2, get_item([1], 5) → None\n```",
                "stub": "# YOUR CODE\ndef get_item(items, index):\n    pass\n",
                "validate": "check_equal('ok', get_item([1, 2], 1), 2)\ncheck_equal('bad index', get_item([1], 5), None)\n",
            },
            {
                "id": 4,
                "title": "parse_age",
                "difficulty": "Medium",
                "description": "Define `parse_age(text)` — return int age if valid and 0–120, else raise `ValueError` with message `\"invalid age\"`.",
                "examples": "```\nparse_age(\"25\") → 25\nparse_age(\"200\") → ValueError\n```",
                "stub": "# YOUR CODE\ndef parse_age(text):\n    pass\n",
                "validate": "check_equal('valid', parse_age('25'), 25)\ntry:\n    parse_age('200')\n    print('✗ parse_age should raise')\nexcept ValueError as e:\n    check_equal('message', str(e), 'invalid age')\n",
            },
            {
                "id": 5,
                "title": "read_key",
                "difficulty": "Easy",
                "description": "Define `read_key(d, key)` — return `d[key]` or `None` on `KeyError`.",
                "examples": '```\nread_key({"a": 1}, "a") → 1, read_key({}, "x") → None\n```',
                "stub": "# YOUR CODE\ndef read_key(d, key):\n    pass\n",
                "validate": 'check_equal("ok", read_key({"a": 1}, "a"), 1)\ncheck_equal("missing", read_key({}, "x"), None)\n',
            },
        ],
    ),
}


if __name__ == "__main__":
    for filename, nb in NOTEBOOKS.items():
        save(filename, nb)
    print("Done.")
