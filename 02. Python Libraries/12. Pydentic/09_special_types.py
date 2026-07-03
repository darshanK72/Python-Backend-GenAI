# 09 — Special types: EmailStr, HttpUrl, Enum, Literal, TypeAdapter
# Run: python 09_special_types.py
# EmailStr needs: pip install email-validator  (already in requirements.txt)

from enum import Enum
from typing import Literal

from pydantic import BaseModel, Field, TypeAdapter, ValidationError

try:
    from pydantic import EmailStr, HttpUrl
except ImportError:
    print("Install: pip install email-validator")
    raise SystemExit(1)


class Role(str, Enum):
    ADMIN = "admin"
    EDITOR = "editor"
    VIEWER = "viewer"


class Account(BaseModel):
    email: EmailStr
    website: HttpUrl | None = None
    role: Role = Role.VIEWER
    theme: Literal["light", "dark"] = "light"


account = Account(email="learner@example.com", website="https://example.com", role="editor")
print("account:", account.model_dump())

try:
    Account(email="not-an-email", theme="blue")
except ValidationError as e:
    print("invalid account:", e.error_count(), "error(s)")

# --- 1. TypeAdapter validates non-model types ---
PositiveIntList = TypeAdapter(list[int])

nums = PositiveIntList.validate_python([1, 2, 3])
print("validated list:", nums)

try:
    PositiveIntList.validate_python([1, "two", 3])
except ValidationError as e:
    print("list validation failed:", e.errors()[0]["msg"])
