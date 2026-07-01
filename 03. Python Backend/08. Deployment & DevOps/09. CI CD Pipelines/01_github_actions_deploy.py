# 01 — GitHub Actions deploy pipeline sample
# Run: python 01_github_actions_deploy.py

WORKFLOW = """
name: deploy-api
on:
  push:
    branches: [main]
jobs:
  build-and-push:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: docker/setup-buildx-action@v3
      - run: docker build -t myapi:${{ github.sha }} .
      - run: echo "Push image to registry, then deploy to server/K8s"
"""

if __name__ == "__main__":
    print("CI/CD flow: test -> build image -> push -> deploy\n")
    print(WORKFLOW.strip())
