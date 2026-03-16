from pydantic import BaseModel
from typing import List


class Deal(BaseModel):
    id: str
    property_id: str
    arv: int | None = None
    mao: int | None = None
    score: int | None = None
    status: str = "active"  # active | expired | sold
    buyer_matches: List[dict] = []


class DealCreate(BaseModel):
    property_id: str
    arv: int | None = None
    mao: int | None = None
    score: int | None = None
