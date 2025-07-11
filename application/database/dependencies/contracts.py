from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import Path
from fastapi import Depends
from fastapi import HTTPException

from application.database import db_helper
from application.database.models import Contract
from application.database.crud import get_contract


async def get_contract_by_id(
	contract_id: Annotated[int, Path],
	session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
) -> Contract:
	contract = await get_contract(
		session=session,
		contract_id=contract_id)

	if contract is not None:
		return contract

	raise HTTPException(status_code=404, detail=f"Contract {contract_id} not found")