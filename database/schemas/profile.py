from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class ProfileBase(BaseModel):
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    referred_by: Optional[int] = None
    referrals: Optional[List[int]] = None
    registered_at: Optional[datetime] = None
    is_blocked: bool = False
    blocked_by: Optional[int] = None
    blocked_at: Optional[datetime] = None
    block_reason: Optional[str] = None

class ProfileCreate(ProfileBase):
    pass

class ProfileUpdate(ProfileBase):
    pass

class Profile(ProfileBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
