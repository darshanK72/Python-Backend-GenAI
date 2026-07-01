# 02 — CI test gate before deploy
# Run: python 02_ci_test_gate.py

PIPELINE = [
    "pip install -r requirements.txt",
    "pytest -v --tb=short",
    "bandit -r app/ -q",
    "docker build -t api:ci .",
    "docker run --rm api:ci python -c \"print('smoke ok')\"",
]

if __name__ == "__main__":
    print("Deploy only if all steps pass:\n")
    for i, step in enumerate(PIPELINE, 1):
        print(f"  {i}. {step}")
