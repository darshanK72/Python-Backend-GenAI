# 01 — Pydantic introduction
# Run: python 01_pydantic_intro.py
# Install: pip install pydantic

import pydantic
from pydantic import BaseModel, ValidationError


print("Pydantic version:", pydantic.__version__)


# --- 1. Why Pydantic? Typed data with automatic validation ---
# Define a schema once; Pydantic checks types and coerces safe values.


class Book(BaseModel):
    title: str
    author: str
    pages: int
    in_stock: bool = True


good = Book(title="Clean Code", author="Robert Martin", pages=464)
print("valid book:", good)
print("as dict:", good.model_dump())

# --- 2. Type coercion (when safe) ---
coerced = Book(title="1984", author="Orwell", pages="328", in_stock="yes")
print("coerced pages type:", type(coerced.pages), coerced.pages)
print("coerced in_stock:", coerced.in_stock)

# --- 3. Invalid data raises ValidationError ---
try:
    Book(title="Test", author="Someone", pages="not-a-number")
except ValidationError as e:
    print("validation failed:", e.error_count(), "error(s)")

# --- 4. Create from a dict (common for JSON/API payloads) ---
payload = {"title": "Dune", "author": "Frank Herbert", "pages": 688}
from_dict = Book.model_validate(payload)
print("from dict:", from_dict.title)
