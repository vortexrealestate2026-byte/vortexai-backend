from datetime import datetime, timedelta
from jose import jwt
from pydantic import BaseModel
from src.core.config import settings


class TokenData(BaseModel):
    user_id: str | None = None


def create_access_token(user_id: str, expires_minutes: int = 60):
    expire = datetime.utcnow() + timedelta(minutes=expires_minutes)

    payload = {
        "sub": user_id,
        "exp": expire
    }

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM
    )
