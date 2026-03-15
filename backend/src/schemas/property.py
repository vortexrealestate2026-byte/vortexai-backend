from pydantic import BaseModel
from typing import Optional


class Property(BaseModel):
    id: str
    address: str
    price: int
    beds: int | None = None
    baths: float | None = None
    sqft: int | None = None
    description: str | None = None
    processed: bool = False


class PropertyCreate(BaseModel):
    address: str
    price: int
    beds: int | None = None
    baths: float | None = None
    sqft: int | None = None
    description: str | None = None
