# Shared database settings for backend lessons
# Loads from .env via python-dotenv

import os
from pathlib import Path

try:
    from dotenv import load_dotenv

    load_dotenv(Path(__file__).resolve().parents[1] / ".env")
except ImportError:
    pass

MYSQL = {
    "host": os.getenv("MYSQL_HOST", "localhost"),
    "port": int(os.getenv("MYSQL_PORT", "3306")),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", ""),
    "database": os.getenv("MYSQL_DATABASE", "learning_db"),
    "charset": "utf8mb4",
}

POSTGRES = {
    "host": os.getenv("POSTGRES_HOST", "localhost"),
    "port": int(os.getenv("POSTGRES_PORT", "5432")),
    "user": os.getenv("POSTGRES_USER", "postgres"),
    "password": os.getenv("POSTGRES_PASSWORD", ""),
    "database": os.getenv("POSTGRES_DATABASE", "learning_db"),
}

MONGODB = {
    "host": os.getenv("MONGODB_HOST", "localhost"),
    "port": int(os.getenv("MONGODB_PORT", "27017")),
    "database": os.getenv("MONGODB_DATABASE", "learning_db"),
}

REDIS = {
    "host": os.getenv("REDIS_HOST", "localhost"),
    "port": int(os.getenv("REDIS_PORT", "6379")),
    "db": int(os.getenv("REDIS_DB", "0")),
    "password": os.getenv("REDIS_PASSWORD") or None,
}

RABBITMQ = {
    "host": os.getenv("RABBITMQ_HOST", "localhost"),
    "port": int(os.getenv("RABBITMQ_PORT", "5672")),
    "user": os.getenv("RABBITMQ_USER", "guest"),
    "password": os.getenv("RABBITMQ_PASSWORD", "guest"),
}
