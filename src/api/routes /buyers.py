om ..schemas.buyer import BuyerCreate, BuyerUpdate

def create_buyer(db, data: BuyerCreate):
    buyer = db.create_buyer(data.dict())
    return buyer

def update_buyer(db, buyer_id: str, data: BuyerUpdate):
    return db.update_buyer(buyer_id, data.dict(exclude_none=True))
