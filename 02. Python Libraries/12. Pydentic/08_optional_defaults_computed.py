# 08 — Optional, defaults, default_factory, computed_field
# Run: python 08_optional_defaults_computed.py

from pydantic import BaseModel, Field, computed_field


class Rectangle(BaseModel):
    width: float = Field(gt=0)
    height: float = Field(gt=0)
    label: str | None = None
    tags: list[str] = Field(default_factory=list)

    @computed_field
    @property
    def area(self) -> float:
        return self.width * self.height

    @computed_field
    @property
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


rect = Rectangle(width=4, height=5, tags=["geometry"])
print("area:", rect.area)
print("perimeter:", rect.perimeter)
print("dump includes computed fields:", rect.model_dump())

# --- 1. Optional vs required ---
minimal = Rectangle(width=2, height=3)
print("label is None:", minimal.label is None)

# --- 2. default_factory runs per instance (not shared) ---
a = Rectangle(width=1, height=1)
b = Rectangle(width=1, height=1)
a.tags.append("first")
print("independent lists:", a.tags, b.tags)
