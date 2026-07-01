# 03 — Blue-green and rolling deploy overview
# Run: python 03_deploy_strategies.py

STRATEGIES = {
    "Rolling": "Replace instances one-by-one; simple, brief mixed versions",
    "Blue-green": "Switch traffic between two full environments; fast rollback",
    "Canary": "Send small % of traffic to new version first",
}

if __name__ == "__main__":
    print("Deployment strategies:\n")
    for name, detail in STRATEGIES.items():
        print(f"  {name:12} {detail}")
