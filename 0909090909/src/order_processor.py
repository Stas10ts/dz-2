from pydantic import BaseModel, validator
from typing import Optional


class Order(BaseModel):
    customer_email: str
    amount: float
    status: str = "new"
    note: Optional[str] = None

    class Config:
        orm_mode = True

    @validator("customer_email")
    def validate_email(cls, value):
        if "@" not in value:
            raise ValueError("Invalid email")
        return value.lower()

    @validator("amount")
    def validate_amount(cls, value):
        if value <= 0:
            raise ValueError("Amount must be positive")
        return value

    def to_dict(self):
        return self.dict()
