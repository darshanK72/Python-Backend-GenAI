# 01 — Docker Compose multi-service stack
# Run: python 01_compose_stack.py
# Then: docker compose up --build
# Test: http://127.0.0.1:8000/health  and  /redis-ping

from pathlib import Path

COMPOSE = Path(__file__).resolve().parent / "docker-compose.yml"

if __name__ == "__main__":
    print("Start stack:")
    print(f"  cd \"{COMPOSE.parent}\"")
    print("  docker compose up --build")
    print("\nServices:")
    print("  api   -> http://127.0.0.1:8000")
    print("  redis -> localhost:6379")
    print("\nStop: docker compose down")
