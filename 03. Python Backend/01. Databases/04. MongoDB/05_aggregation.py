# 05 — Aggregation pipeline
# Run: python 05_aggregation.py

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from db_config import MONGODB

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient(f"mongodb://{MONGODB['host']}:{MONGODB['port']}")
    col = client[MONGODB["database"]]["orders"]

    col.delete_many({})
    col.insert_many(
        [
            {"product": "Pen", "qty": 3, "city": "Pune"},
            {"product": "Notebook", "qty": 2, "city": "Pune"},
            {"product": "Pen", "qty": 1, "city": "Nashik"},
        ]
    )

    pipeline = [
        {"$group": {"_id": "$city", "total_qty": {"$sum": "$qty"}}},
        {"$sort": {"total_qty": -1}},
    ]

    for row in col.aggregate(pipeline):
        print(row)

    client.close()
