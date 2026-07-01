# 04 — Input validation with Pydantic
# Run: python 04_input_validation.py

try:
    from pydantic import BaseModel, EmailStr, Field, ValidationError
except ImportError:
    print("Install: pip install pydantic email-validator")
    raise SystemExit(1)


class SignupForm(BaseModel):
    username: str = Field(min_length=3, max_length=32, pattern=r"^[a-zA-Z0-9_]+$")
    email: EmailStr
    age: int = Field(ge=13, le=120)


if __name__ == "__main__":
    good = SignupForm(username="learner_1", email="learner@example.com", age=25)
    print("Valid:", good.model_dump())

    try:
        SignupForm(username="bad name!", email="not-an-email", age=5)
    except ValidationError as e:
        print("Rejected:", e.error_count(), "errors")
