# 01 — Serverless vs containers decision guide
# Run: python 01_serverless_vs_containers.py

COMPARISON = [
    ("Serverless (Lambda/Functions)", "Pay per invocation, auto-scale, cold starts, time limits"),
    ("Containers (Docker/K8s)", "Full control, long-running workers, you manage scale"),
    ("Managed jobs (Cloud Run Jobs)", "Middle ground for batch workloads"),
]

if __name__ == "__main__":
    print("Choose based on workload shape:\n")
    for name, detail in COMPARISON:
        print(f"  {name}")
        print(f"    {detail}\n")
