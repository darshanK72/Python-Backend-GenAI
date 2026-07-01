# 11 — Nested models
# Run: uvicorn 11_nested_models:app --reload --port 8000
# POST /orders  see sample body in /docs

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Lesson 11 — Nested Models")


class Address(BaseModel):
    street: str
    city: str
    zip_code: str = Field(alias="zipCode")

    model_config = {"populate_by_name": True}


class LineItem(BaseModel):
    sku: str
    quantity: int = Field(ge=1)
    price: float = Field(gt=0)


class OrderCreate(BaseModel):
    customer: str
    shipping_address: Address
    items: list[LineItem]


@app.post("/orders", status_code=201)
def create_order(order: OrderCreate):
    total = sum(item.quantity * item.price for item in order.items)
    return {"order": order.model_dump(), "total": total}
