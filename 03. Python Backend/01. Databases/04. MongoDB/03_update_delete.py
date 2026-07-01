# 03 — Update and delete
# Run: python 03_update_delete.py

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from db_config import MONGODB

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient(f"mongodb://{MONGODB['host']}:{MONGODB['port']}")
    col = client[MONGODB["database"]]["students"]

    col.update_one({"name": "Ravi"}, {"$set": {"marks": 80}})
    print("Modified:", col.count_documents({"name": "Ravi", "marks": 80}))

    col.delete_one({"name": "Asha"})
    print("Remaining:", list(col.find({}, {"_id": 0})))

    client.close()
