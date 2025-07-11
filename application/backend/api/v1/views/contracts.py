from typing import Annotated, Sequence

from fastapi import status
from fastapi import Depends
from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from application.database import db_helper
from application.database.models import Contract
from application.database.crud import get_contracts
from application.database.crud import update_contract
from application.database.crud import create_contract
from application.database.crud import delete_contract
from application.database.dependencies import get_contract_by_id
from application.database.schemas import (
	ContractSchema,
	ContractSchemaCreate,
	ContractSchemaUpdate)


router = APIRouter(tags=["Contracts"])

@router.post(
	"/create",
	response_model=ContractSchema,
	status_code=status.HTTP_201_CREATED)
async def create(
	session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
	contract_in: Annotated[ContractSchemaCreate, Depends()]
):
	return await create_contract(
		session=session,
		contract_in=contract_in)


@router.get(
	"/get/{contract_id}",
	response_model=ContractSchema,
	status_code=status.HTTP_200_OK)
async def get(
	contract: Annotated[ContractSchema, Depends(get_contract_by_id)]
):
	return contract


@router.get(
	"/get_all",
	response_model=Sequence[ContractSchema],
	status_code=status.HTTP_200_OK)
async def get_all(
	session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
):
	return await get_contracts(session=session)


@router.patch(
	"/update/{contract_id}",
	response_model=ContractSchemaUpdate,
	status_code=status.HTTP_200_OK)
async def update(
	session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
	contract_in: Annotated[ContractSchemaUpdate, Depends()],
	contract_model: Annotated[Contract, Depends(get_contract_by_id)]
):
	return await update_contract(
		session=session,
		contract=contract_model,
		contract_in=contract_in)


@router.delete(
	"/delete/{contract_id}",
	status_code=status.HTTP_204_NO_CONTENT)
async def delete(
	session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
	contract: Annotated[Contract, Depends(get_contract_by_id)]
):
	return await delete_contract(
		session=session,
		contract=contract)