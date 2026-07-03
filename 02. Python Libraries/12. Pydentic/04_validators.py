# 04 — field_validator and model_validator
# Run: python 04_validators.py

from pydantic import BaseModel, Field, ValidationError, field_validator, model_validator


class Signup(BaseModel):
    username: str = Field(min_length=3)
    email: str
    password: str = Field(min_length=8)
    confirm_password: str

    @field_validator("username", "email", mode="before")
    @classmethod
    def strip_and_lower(cls, value: str) -> str:
        return value.strip().lower()

    @field_validator("email")
    @classmethod
    def must_contain_at(cls, value: str) -> str:
        if "@" not in value:
            raise ValueError("email must contain @")
        return value

    @model_validator(mode="after")
    def passwords_match(self) -> "Signup":
        if self.password != self.confirm_password:
            raise ValueError("passwords do not match")
        return self


user = Signup(
    username="  Learner  ",
    email="  Learner@Example.COM ",
    password="secret123",
    confirm_password="secret123",
)
print("normalized:", user.model_dump())

try:
    Signup(
        username="learner",
        email="not-an-email",
        password="secret123",
        confirm_password="different",
    )
except ValidationError as e:
    print("signup failed:", e.error_count(), "error(s)")
