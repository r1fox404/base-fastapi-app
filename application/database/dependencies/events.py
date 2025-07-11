from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import Path
from fastapi import Depends
from fastapi import HTTPException

from application.database import db_helper
from application.database.models import Event
from application.database.crud import get_event


async def get_event_by_id(
	event_id: Annotated[int, Path],
	session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
) -> Event:
	event = await get_event(
		session=session,
		event_id=event_id)

	if event is not None:
		return event

	raise HTTPException(status_code=404, detail=f"Event {event_id} not found")