from typing import Annotated, Sequence

from fastapi import status
from fastapi import Depends
from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from application.database import db_helper
from application.database.models import Event
from application.database.crud import get_events
from application.database.crud import update_event
from application.database.crud import create_event
from application.database.crud import delete_event
from application.database.dependencies import get_event_by_id
from application.database.schemas import (
	EventSchema,
	EventSchemaCreate,
	EventSchemaUpdate)


router = APIRouter(tags=["Events"])

@router.post(
	"/create",
	response_model=EventSchema,
	status_code=status.HTTP_201_CREATED)
async def create(
	session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
	event_in: Annotated[EventSchemaCreate, Depends()]
):
	return await create_event(
		session=session,
		event_in=event_in)


@router.get(
	"/get/{event_id}",
	response_model=EventSchema,
	status_code=status.HTTP_200_OK)
async def get(
	event: Annotated[EventSchema, Depends(get_event_by_id)]
):
	return event


@router.get(
	"/get_all",
	response_model=Sequence[EventSchema],
	status_code=status.HTTP_200_OK)
async def get_all(
	session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
):
	return await get_events(session=session)


@router.patch(
	"/update/{event_id}",
	response_model=EventSchemaUpdate,
	status_code=status.HTTP_200_OK)
async def update(
	session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
	event_in: Annotated[EventSchemaUpdate, Depends()],
	event_model: Annotated[Event, Depends(get_event_by_id)]
):
	return await update_event(
		session=session,
		event=event_model,
		event_in=event_in)


@router.delete(
	"/delete/{event_id}",
	status_code=status.HTTP_204_NO_CONTENT)
async def delete(
	session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
	event: Annotated[Event, Depends(get_event_by_id)]
):
	return await delete_event(
		session=session,
		event=event)