# 01 — Type hints (introduction)
# Run: python 01_typing_intro.py
#
# Hints document expected types; optional checking with mypy/pyright.

def greet(name: str) -> str:
    return "Hello, " + name

def average(scores: list[float]) -> float:
    return sum(scores) / len(scores)

print(greet("Darshan"))
print("avg =", average([80, 90, 85]))

# --- 1. Optional and Union (3.10+ can use str | None) ---
from typing import Optional

def find_user(user_id: int) -> Optional[dict]:
    if user_id == 1:
        return {"id": 1, "name": "Darshan"}
    return None

print(find_user(1))
print(find_user(99))

# --- 2. Hints do not enforce at runtime ---
def add(a: int, b: int) -> int:
    return a + b

print(add(1, 2))
print(add("a", "b"))   # still works at runtime

# Use a type checker in real projects for safety.
