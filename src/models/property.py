from pydantic import BaseModel
from typing import Optional


class PropertyBase(BaseModel):
    address: str
    price: int
    beds: Optional[int] = None
    baths: Optional[float] = None
    sqft: Optional[int] = None
    description: Optional[str] = None


class PropertyCreate(PropertyBase):
    pass


class PropertyUpdate(BaseModel):
    address: Optional[str] = None
    price: Optional[int] = None
    beds: Optional[int] = None
    baths: Optional[float] = None
    sqft: Optional[int] = None
    description: Optional[str] = None
    processed: Optional[bool] = None


class Property(PropertyBase):
    id: str
    processed: bool = False
