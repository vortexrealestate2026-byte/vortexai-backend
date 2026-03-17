from fastapi import APIRouter

router = APIRouter(prefix="/api/buyers", tags=["buyers"])


@router.get("/")
def get_buyers():
    return {"buyers": []}


@router.post("/")
def create_buyer(data: dict):
    return {"message": "buyer created"}
