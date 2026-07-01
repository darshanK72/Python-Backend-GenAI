# 03 — Sample GitHub Actions workflow snippet
# Run: python 03_github_actions_sample.py

WORKFLOW = """
name: backend-tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - run: pytest "03. Python Backend/07. Testing" -v --tb=short
"""

if __name__ == "__main__":
    print("Save as .github/workflows/backend-tests.yml:\n")
    print(WORKFLOW.strip())
