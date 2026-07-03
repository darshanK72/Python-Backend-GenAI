# 02 — Field() and built-in constraints
# Run: python 02_fields_and_constraints.py

from pydantic import BaseModel, Field, ValidationError


class Product(BaseModel):
    sku: str = Field(min_length=3, max_length=20, pattern=r"^[A-Z0-9-]+$")
    name: str = Field(min_length=1, max_length=100)
    price: float = Field(gt=0, description="Price must be positive")
    discount_pct: float = Field(ge=0, le=100, default=0)
    tags: list[str] = Field(default_factory=list, max_length=5)


valid = Product(sku="SKU-001", name="Keyboard", price=49.99, tags=["electronics"])
print("valid product:", valid.model_dump())

# --- 1. String pattern and length ---
try:
    Product(sku="bad sku!", name="Mouse", price=10)
except ValidationError as e:
    print("sku rejected:", e.errors()[0]["msg"])

# --- 2. Numeric bounds ---
try:
    Product(sku="SKU-002", name="Free item", price=0)
except ValidationError as e:
    print("price rejected:", e.errors()[0]["msg"])

# --- 3. Field metadata (useful in OpenAPI / docs) ---
print("price description:", Product.model_fields["price"].description)
