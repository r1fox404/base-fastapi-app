from typing import List
from datetime import datetime

from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.dialects.postgresql import ARRAY

from application.database.models import Base
from application.core.enums import EventStateType


class Event(Base):
	__tablename__ = "events"

	id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

	author_telegram_id: Mapped[int] = mapped_column(BigInteger, nullable=False)

	date: Mapped[str] = mapped_column(String(35), nullable=False)
	time: Mapped[str] = mapped_column(String(35), nullable=False)
	title: Mapped[str] = mapped_column(String(250), nullable=False)
	tickets_all: Mapped[int] = mapped_column(Integer, nullable=False)
	tickets_left: Mapped[int] = mapped_column(Integer, nullable=False)
	location: Mapped[str] = mapped_column(String(250), nullable=False)
	headliner: Mapped[str] = mapped_column(String(250), nullable=False)
	cost_per_ticket: Mapped[int] = mapped_column(Integer, nullable=False)
	members_telegram_id: Mapped[List[int]] = mapped_column(ARRAY(BigInteger), nullable=True)
	state: Mapped[EventStateType]  = mapped_column(String, default=EventStateType.REGISTRATION, nullable=True)

	created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
	updated_at: Mapped[datetime] = mapped_column(DateTime, onupdate=datetime.now, nullable=True)