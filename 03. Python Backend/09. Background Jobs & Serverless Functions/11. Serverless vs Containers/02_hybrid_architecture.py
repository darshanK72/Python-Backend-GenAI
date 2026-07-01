# 02 — When to combine API + queue + serverless
# Run: python 02_hybrid_architecture.py

if __name__ == "__main__":
    print("Common hybrid pattern:")
    print("  FastAPI (container) -> enqueue Celery/RQ -> worker container")
    print("  OR")
    print("  API Gateway -> Lambda (short) -> SQS -> Lambda worker (long tasks)")
    print("\nUse containers for steady API traffic; serverless for spiky/batch work.")
