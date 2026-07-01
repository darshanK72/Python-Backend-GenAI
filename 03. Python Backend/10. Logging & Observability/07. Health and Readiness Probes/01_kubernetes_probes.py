# 01 — Health vs readiness for Kubernetes
# Run: python 01_kubernetes_probes.py

if __name__ == "__main__":
    print("Kubernetes probes:")
    print("  livenessProbe  -> /health  (restart if failing)")
    print("  readinessProbe -> /ready   (remove from service if failing)")
    print("  startupProbe   -> slow-start apps")
    print("\nRun: uvicorn app:app --port 8022")
