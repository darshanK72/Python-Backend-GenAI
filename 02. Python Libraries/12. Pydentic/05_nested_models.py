# 05 — Nested models, lists, and optional fields
# Run: python 05_nested_models.py

from pydantic import BaseModel, Field


class Address(BaseModel):
    street: str
    city: str
    country: str = "India"


class Contact(BaseModel):
    email: str
    phone: str | None = None


class Employee(BaseModel):
    id: int
    name: str
    address: Address
    contact: Contact
    skills: list[str] = Field(default_factory=list)


employee = Employee(
    id=101,
    name="Priya",
    address={"street": "12 MG Road", "city": "Pune"},
    contact={"email": "priya@example.com"},
    skills=["Python", "SQL"],
)

print("employee city:", employee.address.city)
print("skills count:", len(employee.skills))
print("full dump:\n", employee.model_dump())

# --- 1. Partial nested update via model_validate ---
updated = employee.model_copy(update={"name": "Priya Sharma"})
print("updated name:", updated.name)
