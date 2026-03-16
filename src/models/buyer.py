from pydantic import BaseModel, EmailStr
from typing import List


class BuyerBase(BaseModel):
    name: str
    email: EmailStr
    phone: str | None = None
    criteria: List[str] = []


class BuyerCreate(BuyerBase):
    pass


class BuyerUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    phone: str | None = None
    criteria: List[str] | None = None


class Buyer(BuyerBase):
    id: str
