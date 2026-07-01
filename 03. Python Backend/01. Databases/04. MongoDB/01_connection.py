# 01 — Connect to MongoDB
# Run: python 01_connection.py
#
# Setup: MongoDB on localhost:27017, pip install pymongo

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from db_config import MONGODB

try:
    from pymongo import MongoClient
    from pymongo.errors import PyMongoError
except ImportError:
    print("Install: pip install pymongo")
    raise SystemExit(1)

uri = f"mongodb://{MONGODB['host']}:{MONGODB['port']}"

if __name__ == "__main__":
    try:
        client = MongoClient(uri, serverSelectionTimeoutMS=3000)
        client.admin.command("ping")
        db = client[MONGODB["database"]]
        print("Connected to MongoDB")
        print("Database:", db.name)
        print("Collections:", db.list_collection_names())
        client.close()
    except PyMongoError as e:
        print("MongoDB error:", e)
        print("Start MongoDB and check .env settings.")
