# 02 — GCF Pub/Sub background trigger overview
# Run: python 02_gcf_pubsub.py

if __name__ == "__main__":
    print("Cloud Functions can subscribe to Pub/Sub topics.")
    print("Event-driven: message published -> function invoked -> process job")
    print("\nGood for: image resize, webhook fan-out, ETL steps")
