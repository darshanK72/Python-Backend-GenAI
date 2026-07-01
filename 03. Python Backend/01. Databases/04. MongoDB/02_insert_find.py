# 02 — Insert and find documents
# Run: python 02_insert_find.py

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from db_config import MONGODB

from pymongo import MongoClient

COLLECTION = "students"

if __name__ == "__main__":
    client = MongoClient(f"mongodb://{MONGODB['host']}:{MONGODB['port']}")
    db = client[MONGODB["database"]]
    col = db[COLLECTION]

    col.delete_many({})  # reset lesson data
    col.insert_many(
        [
            {"name": "Asha", "marks": 88, "city": "Pune"},
            {"name": "Ravi", "marks": 76, "city": "Nashik"},
        ]
    )

    print("All documents:")
    for doc in col.find({}, {"_id": 0}):
        print(doc)

    print("Pune students:")
    for doc in col.find({"city": "Pune"}, {"_id": 0}):
        print(doc)

    client.close()
