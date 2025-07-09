from typing import Optional
from pydantic import BaseModel
from .profile import Profile
from core.roles import UserRole


class UserBase(BaseModel):
    telegram_id: int
    role: str = UserRole.USER


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: int
    profile: Optional[Profile] = None

    class Config:
        orm_mode = True
