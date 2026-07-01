# 04 — Query operators
# Run: python 04_query_operators.py

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from db_config import MONGODB

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient(f"mongodb://{MONGODB['host']}:{MONGODB['port']}")
    col = client[MONGODB["database"]]["students"]

    col.delete_many({})
    col.insert_many(
        [
            {"name": "Asha", "marks": 88},
            {"name": "Ravi", "marks": 76},
            {"name": "Meera", "marks": 92},
        ]
    )

    print("marks >= 85:")
    for doc in col.find({"marks": {"$gte": 85}}, {"_id": 0}):
        print(doc)

    print("names in list:")
    for doc in col.find({"name": {"$in": ["Asha", "Meera"]}}, {"_id": 0}):
        print(doc)

    client.close()
