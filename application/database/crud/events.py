from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from application.database.models import Event
from application.database.schemas import (
	EventSchemaCreate,
	EventSchemaUpdate)


async def create_event(
	session: AsyncSession,
	event_in: EventSchemaCreate,
) -> Event:
	event = Event(**event_in.model_dump())
	session.add(event)
	await session.commit()
	return event


async def get_event(
	session: AsyncSession,
	event_id: int
) -> Event | None:
	return await session.get(Event, event_id)


async def get_events(
	session: AsyncSession
) -> Sequence[Event] | None:
	stmt = select(Event)
	result = await session.scalars(stmt)
	return result.all()


async def update_event(
	session: AsyncSession,
	event: Event,
	event_in: EventSchemaUpdate,
) -> Event:
	for k, v in event_in.model_dump(exclude_none=True).items():
		setattr(event, k, v)
	await session.commit()
	return event


async def delete_event(
	session: AsyncSession,
	event: Event
) -> None:
	await session.delete(event)
	await session.commit()