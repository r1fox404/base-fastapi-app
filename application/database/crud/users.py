from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


from application.database.models import User
from application.database.schemas import (
	UserSchema,
	UserSchemaCreate,
	UserSchemaUpdate,
)


async def create_user(
	session: AsyncSession,
	user_in: UserSchemaCreate,
) -> User:
	user = User(**user_in.model_dump())
	session.add(user)
	await session.commit()
	return user


async def get_user(
	session: AsyncSession,
	telegram_id: int
) -> User | None:
	return await session.get(User, telegram_id)


async def get_users(
	session: AsyncSession
) -> Sequence[User] | None:
	stmt = select(User)
	result = await session.scalars(stmt)
	return result.all()


async def update_user(
	session: AsyncSession,
	user: User,
	user_in: UserSchemaUpdate,
) -> User:
	for k, v in user_in.model_dump(exclude_none=True).items():
		setattr(user, k, v)
	await session.commit()
	return user


async def delete_user(
	session: AsyncSession,
	user: User
) -> None:
	await session.delete(user)
	await session.commit()