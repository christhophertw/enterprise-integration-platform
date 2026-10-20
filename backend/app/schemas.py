from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field, field_validator


class CustomerCreate(BaseModel):
    name: str = Field(min_length=1, max_length=150)
    email: str = Field(min_length=3, max_length=255, pattern=r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


class CustomerRead(CustomerCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int


class ProductCreate(BaseModel):
    sku: str = Field(min_length=1, max_length=50)
    name: str = Field(min_length=1, max_length=150)
    price: Decimal = Field(ge=0, max_digits=12, decimal_places=2)
    active: bool = True

    @field_validator("sku", "name")
    @classmethod
    def strip_and_require_text(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Must not be blank")
        return value

    @field_validator("sku")
    @classmethod
    def normalize_sku(cls, value: str) -> str:
        return value.upper()


class ProductRead(ProductCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
