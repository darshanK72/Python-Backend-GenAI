# Capstone — dockerized Notes API
# Run: python 01_capstone_walkthrough.py
# Then: docker compose up --build

from pathlib import Path

HERE = Path(__file__).resolve().parent

if __name__ == "__main__":
    print("Deployment capstone — full stack:\n")
    print(f"  Folder: {HERE}")
    print("  1. docker compose up --build")
    print("  2. Open http://127.0.0.1:8000/health")
    print("  3. POST /notes with JSON {\"title\":\"Deployed!\"}")
    print("  4. Check /ready includes redis status")
    print("\nFiles: Dockerfile, docker-compose.yml, app/main.py")
