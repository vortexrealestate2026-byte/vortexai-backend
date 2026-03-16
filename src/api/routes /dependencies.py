from fastapi import Depends, HTTPException
from jose import jwt, JWTError
from .db.base import get_db
from .config import settings
from .auth import TokenData

def get_current_user(token: str, db=Depends(get_db)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token")
        return db.get_user(user_id)
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
