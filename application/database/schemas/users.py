from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict

from application.core.enums import UserStates, UserRole


class UserSchemaBase(BaseModel):
	telegram_id: int

	username: Optional[str] = None
	first_name: Optional[str] = None
	last_name: Optional[str] = None
	phone_number: Optional[str] = None

	state: UserStates = UserStates("REGISTERED")
	role: UserRole = UserRole("USER")
	blocked_by: Optional[int] = None
	block_reason: Optional[str] = None


class UserSchemaCreate(UserSchemaBase):
	pass


class UserSchemaUpdate(UserSchemaCreate):
	username: Optional[str] = None
	first_name: Optional[str] = None
	last_name: Optional[str] = None
	phone_number: Optional[str] = None
	state: Optional[UserStates] = None
	blocked_by: Optional[int] = None
	block_reason: Optional[str] = None
	role: Optional[UserRole] = None


class UserSchema(UserSchemaBase):
	model_config = ConfigDict(from_attributes=True)

	created_at: datetime