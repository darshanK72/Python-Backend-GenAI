# 01 — Testing pyramid for backend apps
# Run: python 01_testing_pyramid.py

PYRAMID = [
    ("Unit", "Fast, many — test functions/classes in isolation"),
    ("Integration", "Medium — DB, cache, message queues with real or test doubles"),
    ("API / Contract", "Fewer — HTTP endpoints, request/response shape"),
    ("End-to-end", "Fewest — full stack through browser or external client"),
]

if __name__ == "__main__":
    print("Backend testing pyramid (bottom = most tests):\n")
    for level, detail in PYRAMID:
        print(f"  {level:12} {detail}")
    print("\nStart with unit tests for business logic, then API tests for routes.")
