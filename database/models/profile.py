from datetime import datetime
from typing import List, Optional
from sqlalchemy import Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy.types import String, BigInteger
from sqlalchemy.dialects.postgresql import ARRAY
from .base import Base
from .user import User


class Profile(Base):
    __tablename__ = "profiles"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[Optional[str]] = mapped_column(String(120), nullable=True)
    first_name: Mapped[Optional[str]] = mapped_column(String(120), nullable=True)
    last_name: Mapped[Optional[str]] = mapped_column(String(120), nullable=True)
    referred_by: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True)
    referrals: Mapped[Optional[List[int]]] = mapped_column(ARRAY(BigInteger), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    is_blocked: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    blocked_by: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True)
    blocked_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    block_reason: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)
    user: Mapped["User"] = relationship("User", back_populates="profile")
