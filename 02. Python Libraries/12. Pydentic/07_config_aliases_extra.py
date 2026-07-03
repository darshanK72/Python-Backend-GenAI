# 07 — model_config, aliases, and extra fields
# Run: python 07_config_aliases_extra.py

from pydantic import BaseModel, ConfigDict, Field, ValidationError


class ApiUser(BaseModel):
    # Accept camelCase from JSON while using snake_case in Python
    model_config = ConfigDict(populate_by_name=True, str_strip_whitespace=True)

    user_id: int = Field(alias="userId")
    full_name: str = Field(alias="fullName")
    is_active: bool = Field(default=True, alias="isActive")


# --- 1. Parse external JSON with aliases ---
payload = {
    "userId": 42,
    "fullName": "  Darshan  ",
    "isActive": False,
}
user = ApiUser.model_validate(payload)
print("python names:", user.user_id, user.full_name, user.is_active)
print("dump by alias:", user.model_dump(by_alias=True))

# --- 2. Extra fields policy ---
class StrictItem(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    qty: int


StrictItem(name="Pen", qty=2)
print("strict item ok")

try:
    StrictItem(name="Pen", qty=2, color="blue")
except ValidationError as e:
    print("extra field rejected:", e.errors()[0]["type"])
