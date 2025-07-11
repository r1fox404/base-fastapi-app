from typing import Annotated, Sequence

from fastapi import status
from fastapi import Depends
from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from application.database import db_helper
from application.database.models import User
from application.database.crud import get_users
from application.database.crud import update_user
from application.database.crud import create_user
from application.database.crud import delete_user
from application.database.dependencies import get_user_by_telegram_id
from application.database.schemas import (
	UserSchema,
	UserSchemaCreate,
	UserSchemaUpdate)


router = APIRouter(tags=["Users"])


@router.post(
	"/create",
	response_model=UserSchema,
	status_code=status.HTTP_201_CREATED)
async def create(
	session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
	user_in: Annotated[UserSchemaCreate, Depends()]
):
	return await create_user(
		session=session,
		user_in=user_in)


@router.get(
	"/get/{telegram_id}",
	response_model=UserSchema,
	status_code=status.HTTP_200_OK)
async def get(
	user: Annotated[UserSchema, Depends(get_user_by_telegram_id)]
):
	return user


@router.get(
	"/get_all",
	response_model=Sequence[UserSchema],
	status_code=status.HTTP_200_OK)
async def get_all(
	session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
):
	return await get_users(session=session)


@router.patch(
	"/update/{telegram_id}",
	response_model=UserSchema,
	status_code=status.HTTP_200_OK)
async def update(
	session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
	user_in: Annotated[UserSchemaUpdate, Depends()],
	user_model: Annotated[User, Depends(get_user_by_telegram_id)]
):
	return await update_user(
		session=session,
		user=user_model,
		user_in=user_in)


@router.delete(
	"/delete/{telegram_id}",
	status_code=status.HTTP_204_NO_CONTENT)
async def delete(
	session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
	user: Annotated[User, Depends(get_user_by_telegram_id)]
):
	return await delete_user(
		session=session,
		user=user)