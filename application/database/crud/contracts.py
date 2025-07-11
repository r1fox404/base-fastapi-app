from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from application.database.models import Contract
from application.database.schemas import (
	ContractSchemaCreate,
	ContractSchemaUpdate)


async def create_contract(
	session: AsyncSession,
	contract_in: ContractSchemaCreate,
) -> Contract:
	contract = Contract(**contract_in.model_dump())
	session.add(contract)
	await session.commit()
	return contract


async def get_contract(
	session: AsyncSession,
	contract_id: int
) -> Contract | None:
	return await session.get(Contract, contract_id)


async def get_contracts(
	session: AsyncSession
) -> Sequence[Contract] | None:
	stmt = select(Contract)
	result = await session.scalars(stmt)
	return result.all()


async def update_contract(
	session: AsyncSession,
	contract: Contract,
	contract_in: ContractSchemaUpdate,
) -> Contract:
	for k, v in contract_in.model_dump(exclude_none=True).items():
		setattr(contract, k, v)
	await session.commit()
	return contract


async def delete_contract(
	session: AsyncSession,
	contract: Contract
) -> None:
	await session.delete(contract)
	await session.commit()