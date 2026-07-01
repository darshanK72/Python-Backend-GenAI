# 01 — Liveness vs readiness probes
# Run: python 01_health_vs_ready.py

if __name__ == "__main__":
    print("Liveness  (/health): restart container if process is stuck/dead")
    print("Readiness (/ready):  remove from load balancer if DB/cache is down")
    print("\nKubernetes example:")
    print("  livenessProbe:  httpGet: /health")
    print("  readinessProbe: httpGet: /ready")
    print("\nStart lesson app:")
    print("  uvicorn app:app --port 8000")
