from fastapi import APIRouter

router = APIRouter(prefix="/api/deals", tags=["deals"])


@router.get("/")
def get_deals():
    return {"deals": []}


@router.post("/")
def create_deal(data: dict):
    return {"message": "deal created"}


@router.get("/{deal_id}")
def get_deal(deal_id: int):
    return {"id": deal_id}
