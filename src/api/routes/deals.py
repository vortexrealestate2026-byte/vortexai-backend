from fastapi import APIRouter

router = APIRouter(prefix="/api/deals", tags=["deals"])

deals_db = []

@router.get("/")
def get_deals():
    return deals_db

@router.post("/")
def create_deal(data: dict):
    deals_db.append(data)
    return {"message": "deal created", "deal": data}

@router.get("/{deal_id}")
def get_deal(deal_id: int):
    if deal_id < len(deals_db):
        return deals_db[deal_id]
    return {"error": "deal not found"}
