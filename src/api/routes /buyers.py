from fastapi import APIRouter

router = APIRouter(prefix="/buyers", tags=["buyers"])

buyers_db = []

@router.get("/")
def get_buyers():
    return {"buyers": buyers_db}

@router.post("/")
def add_buyer(data: dict):
    buyers_db.append(data)
    return {"message": "buyer added", "buyer": data}
