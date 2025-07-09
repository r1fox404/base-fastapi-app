from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy.types import String, BigInteger
from .profile import Profile
from .base import Base
from core.roles import UserRole


class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    telegram_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    role: Mapped[str] = mapped_column(String(20), default=UserRole.USER)
    profile: Mapped[Optional[Profile]] = relationship(
        "Profile",
        back_populates="user",
        uselist=False
    )
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
