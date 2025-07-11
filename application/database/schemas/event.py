from typing import List
from typing import Optional
from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict

from application.core.enums import EventStateType


class EventSchemaBase(BaseModel):
	date: str
	time: str
	title: str
	location: str
	headliner: str
	tickets_all: int
	tickets_left: int
	cost_per_ticket: int
	author_telegram_id: int
	state: EventStateType = EventStateType.REGISTRATION


class EventSchemaCreate(EventSchemaBase):
	pass


class EventSchemaUpdate(EventSchemaCreate):
	date: Optional[str] = None
	time: Optional[str] = None
	title: Optional[str] = None
	location: Optional[str] = None
	headliner: Optional[str] = None
	tickets_all: Optional[int] = None
	tickets_left: Optional[int] = None
	cost_per_ticket: Optional[int] = None
	state: Optional[EventStateType] = None
	author_telegram_id: Optional[int] = None
	members_telegram_id: Optional[List[int]] = None


class EventSchema(EventSchemaBase):
	model_config = ConfigDict(from_attributes=True)

	id: int
	created_at: datetime
	updated_at: Optional[datetime]
	members_telegram_id: Optional[List[int]]