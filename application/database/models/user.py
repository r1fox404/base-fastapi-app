from datetime import datetime
from typing import Optional, TYPE_CHECKING

from sqlalchemy import DateTime, Boolean
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy.types import String, BigInteger
from application.core.enums import UserRole, UserStates
from application.database.models import Base


class User(Base):
    __tablename__ = "users"

    telegram_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)

    username: Mapped[Optional[str]] = mapped_column(String(120), nullable=True)
    first_name: Mapped[Optional[str]] = mapped_column(String(120), nullable=True)
    last_name: Mapped[Optional[str]] = mapped_column(String(120), nullable=True)
    phone_number: Mapped[Optional[str]] = mapped_column(String(120), nullable=True)

    state: Mapped[UserStates] = mapped_column(String, default=UserStates("REGISTERED"))
    role: Mapped[UserRole] = mapped_column(String, default=UserRole("USER"))
    blocked_by: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True)
    block_reason: Mapped[Optional[str]] = mapped_column(String(250), nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())