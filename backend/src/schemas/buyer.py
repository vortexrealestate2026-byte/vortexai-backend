from pydantic import BaseModel, EmailStr
from typing import List


class Buyer(BaseModel):
    id: str
    name: str
    email: EmailStr
    phone: str | None = None
    criteria: List[str] = []


class BuyerCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str | None = None
    criteria: List[str] = []


class BuyerMatchResult(BaseModel):
    buyer_id: str
    buyer_name: str
    match_score: int
    reason: str
