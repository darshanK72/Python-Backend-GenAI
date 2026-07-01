# 01 — Redis vs RabbitMQ as Celery broker
# Run: python 01_broker_comparison.py

BROKERS = {
    "Redis": {
        "url": "redis://localhost:6379/1",
        "pros": "Simple, already used for cache",
        "cons": "Less ideal for very high fan-out",
    },
    "RabbitMQ": {
        "url": "amqp://guest:guest@localhost:5672//",
        "pros": "Mature messaging, routing, durability",
        "cons": "Extra service to operate",
    },
}

if __name__ == "__main__":
    print("Celery broker options:\n")
    for name, info in BROKERS.items():
        print(f"  {name}")
        print(f"    URL: {info['url']}")
        print(f"    Pros: {info['pros']}")
        print(f"    Cons: {info['cons']}\n")
