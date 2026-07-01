# 02 — Integration vs unit: when to use each
# Run: python 02_integration_vs_unit.py

if __name__ == "__main__":
    print("Unit test:")
    print("  - Mock DB and test service rules only")
    print("  - Fast, many tests\n")
    print("Integration test:")
    print("  - Real SQLite in-memory or test database")
    print("  - Catches SQL mistakes and wiring bugs")
    print("  - Slower — use fewer, focused cases")
