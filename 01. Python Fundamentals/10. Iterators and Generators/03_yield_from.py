# 03 — yield from (delegate to another iterable)
# Run: python 03_yield_from.py

def chain_lists(a, b):
    yield from a
    yield from b

combined = list(chain_lists([1, 2], [3, 4]))
print("combined:", combined)

# --- 1. Flatten one level ---
def flatten(nested):
    for sub in nested:
        yield from sub

matrix = [[1, 2], [3, 4], [5]]
print("flat:", list(flatten(matrix)))
