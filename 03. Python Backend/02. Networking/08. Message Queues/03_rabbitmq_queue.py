# 03 — RabbitMQ simple queue
# Run: python 03_rabbitmq_queue.py
# Requires RabbitMQ on localhost:5672
# Install: pip install pika

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

try:
    import pika
except ImportError:
    print("Install: pip install pika")
    raise SystemExit(1)

from db_config import RABBITMQ

QUEUE = "lesson_simple_queue"


def connect():
    params = pika.ConnectionParameters(
        host=RABBITMQ["host"],
        port=RABBITMQ["port"],
        credentials=pika.PlainCredentials(RABBITMQ["user"], RABBITMQ["password"]),
    )
    return pika.BlockingConnection(params)


if __name__ == "__main__":
    try:
        connection = connect()
    except pika.exceptions.AMQPConnectionError as e:
        print("RabbitMQ error:", e)
        raise SystemExit(1)

    channel = connection.channel()
    channel.queue_declare(queue=QUEUE, durable=False)

    for body in ["job-1", "job-2"]:
        channel.basic_publish(exchange="", routing_key=QUEUE, body=body)
        print("Published:", body)

    print("Consuming...")
    for _ in range(2):
        method, properties, body = channel.basic_get(queue=QUEUE, auto_ack=True)
        if body:
            print("Consumed:", body.decode())

    connection.close()
    print("Done")
