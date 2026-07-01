# 02 — Idempotent task processing
# Run: python 02_idempotent_tasks.py

PROCESSED: set[str] = {}


def process_payment(event_id: str, amount: float) -> dict:
    if event_id in PROCESSED:
        return {"event_id": event_id, "status": "already_processed"}
    PROCESSED.add(event_id)
    return {"event_id": event_id, "status": "charged", "amount": amount}


if __name__ == "__main__":
    print(process_payment("evt_100", 49.99))
    print(process_payment("evt_100", 49.99))  # duplicate webhook — safe
