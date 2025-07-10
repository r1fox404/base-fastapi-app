from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import Path
from fastapi import Depends
from fastapi import HTTPException

from application.database import db_helper
from application.database.models import User
from application.database.crud import get_user


async def get_user_by_telegram_id(
	telegram_id: Annotated[int, Path],
	session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
) -> User:
	user = await get_user(
		session=session,
		telegram_id=telegram_id)

	if user is not None:
		return user

	raise HTTPException(status_code=404, detail=f"User {telegram_id} not found")