from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict

from application.core.enums import UserStateType, UserRoleType


class UserSchemaBase(BaseModel):
	telegram_id: int

	username: Optional[str] = None
	first_name: Optional[str] = None
	last_name: Optional[str] = None
	phone_number: Optional[str] = None

	state: UserStateType = UserStateType.REGISTERED
	role: UserRoleType = UserRoleType.USER
	blocked_by: Optional[int] = None
	block_reason: Optional[str] = None


class UserSchemaCreate(UserSchemaBase):
	pass


class UserSchemaUpdate(UserSchemaCreate):
	username: Optional[str] = None
	first_name: Optional[str] = None
	last_name: Optional[str] = None
	phone_number: Optional[str] = None
	state: Optional[UserStateType] = None
	blocked_by: Optional[int] = None
	block_reason: Optional[str] = None
	role: Optional[UserRoleType] = None


class UserSchema(UserSchemaBase):
	model_config = ConfigDict(from_attributes=True)

	created_at: datetime
	updated_at: Optional[datetime]