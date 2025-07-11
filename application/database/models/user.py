from datetime import datetime
from typing import List
from typing import Optional

from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from application.database.models import Base
from application.core.enums import UserRoleType
from application.core.enums import UserStateType


class User(Base):
    __tablename__ = "users"

    telegram_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)

    username: Mapped[Optional[str]] = mapped_column(String(120), nullable=True)
    blocked_by: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True)
    last_name: Mapped[Optional[str]] = mapped_column(String(120), nullable=True)
    role: Mapped[UserRoleType] = mapped_column(String, default=UserRoleType.USER)
    first_name: Mapped[Optional[str]] = mapped_column(String(120), nullable=True)
    phone_number: Mapped[Optional[str]] = mapped_column(String(120), nullable=True)
    block_reason: Mapped[Optional[str]] = mapped_column(String(250), nullable=True)
    state: Mapped[UserStateType] = mapped_column(String, default=UserStateType.REGISTERED)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, onupdate=datetime.now, nullable=True)