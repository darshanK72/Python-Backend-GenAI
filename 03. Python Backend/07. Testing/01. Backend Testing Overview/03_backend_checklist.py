# 03 — Backend test checklist
# Run: python 03_backend_checklist.py

CHECKLIST = [
    "Happy path returns expected status and JSON",
    "Validation errors return 422/400 with clear messages",
    "Auth required routes reject missing/invalid credentials",
    "Database tests use isolated DB or roll back transactions",
    "External APIs are mocked in unit tests",
    "Tests do not depend on execution order",
]

if __name__ == "__main__":
    print("Before shipping a backend feature, verify:\n")
    for i, item in enumerate(CHECKLIST, 1):
        print(f"  {i}. {item}")
