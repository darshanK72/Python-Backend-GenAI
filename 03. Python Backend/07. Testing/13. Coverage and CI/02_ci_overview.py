# 02 — CI pipeline overview for backend tests
# Run: python 02_ci_overview.py

STEPS = [
    "checkout code",
    "setup Python + pip install -r requirements.txt",
    "run lint (optional): ruff, bandit",
    "run tests: pytest -v",
    "run coverage gate: pytest --cov=src --cov-fail-under=80",
    "build/deploy only if tests pass",
]

if __name__ == "__main__":
    print("Typical GitHub Actions / CI job:\n")
    for i, step in enumerate(STEPS, 1):
        print(f"  {i}. {step}")
