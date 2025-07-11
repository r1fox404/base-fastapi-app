from datetime import datetime

from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from application.database.models import Base
from application.core.enums import ContractStateType
from application.core.enums import ContractRejectType


class Contract(Base):
	__tablename__ = "contracts"

	id: Mapped[int] = mapped_column(primary_key=True)

	price: Mapped[int] = mapped_column(Integer, nullable=False)
	tickets: Mapped[int] = mapped_column(Integer, nullable=False)
	event_id: Mapped[int] = mapped_column(Integer, nullable=False)
	customer_telegram_id: Mapped[int] = mapped_column(BigInteger, nullable=False)

	rejected_by: Mapped[ContractRejectType] = mapped_column(String, nullable=True)
	state: Mapped[ContractStateType] = mapped_column(String, default=ContractStateType.PENDING, nullable=False)

	created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
	updated_at: Mapped[datetime] = mapped_column(DateTime, onupdate=datetime.now, nullable=True)