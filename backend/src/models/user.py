from pydantic import BaseModel, EmailStr
from typing import Optional
from .enums import UserRole


class UserBase(BaseModel):
    email: EmailStr
    name: Optional[str] = None
    role: UserRole = UserRole.wholesaler


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    name: Optional[str] = None
    role: Optional[UserRole] = None


class User(BaseModel):
    id: str
    email: EmailStr
    name: Optional[str] = None
    role: UserRole
