# 02 — Deep health check pattern
# Run: python 02_deep_health_check.py

def check_database() -> bool:
    return True


def check_redis() -> bool:
    return True


def deep_health() -> dict:
    db_ok = check_database()
    redis_ok = check_redis()
    healthy = db_ok and redis_ok
    return {
        "status": "ready" if healthy else "degraded",
        "checks": {"database": db_ok, "redis": redis_ok},
    }


if __name__ == "__main__":
    print(deep_health())
