from typing import List
from typing import Optional
from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict

from application.core.enums import ContractStateType
from application.core.enums import ContractRejectType


class ContractSchemaBase(BaseModel):
	price: int
	tickets: int
	event_id: int
	customer_telegram_id: int
	rejected_by: Optional[ContractRejectType] = None
	state: ContractStateType = ContractStateType.PENDING


class ContractSchemaCreate(ContractSchemaBase):
	pass


class ContractSchemaUpdate(ContractSchemaCreate):
	price: Optional[int] = None
	tickets: Optional[int] = None
	event_id: Optional[int] = None
	state: Optional[ContractStateType] = None
	customer_telegram_id: Optional[int] = None
	rejected_by: Optional[ContractRejectType] = None


class ContractSchema(ContractSchemaBase):
	model_config = ConfigDict(from_attributes=True)

	id: int
	created_at: datetime
	updated_at: Optional[datetime]