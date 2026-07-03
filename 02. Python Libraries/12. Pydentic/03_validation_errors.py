# 03 — ValidationError: reading and handling failures
# Run: python 03_validation_errors.py

from pydantic import BaseModel, Field, ValidationError


class UserProfile(BaseModel):
    username: str = Field(min_length=3, max_length=32)
    age: int = Field(ge=13, le=120)
    score: float = Field(ge=0, le=100)


def register(raw: dict) -> UserProfile | None:
    try:
        return UserProfile.model_validate(raw)
    except ValidationError as e:
        print(f"Rejected {e.error_count()} error(s):")
        for err in e.errors():
            loc = ".".join(str(part) for part in err["loc"])
            print(f"  - {loc}: {err['msg']}")
        return None


ok = register({"username": "learner", "age": 25, "score": 88.5})
print("registered:", ok.model_dump() if ok else None)

print()
register({"username": "ab", "age": 200, "score": -5})

# --- 1. JSON-friendly error export (APIs often return this shape) ---
try:
    UserProfile(username="x", age=10, score=50)
except ValidationError as e:
    print("\nerrors JSON:", e.errors())
