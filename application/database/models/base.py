from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase

from application.core.settings import settings


class Base(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(naming_convention=settings.db.naming_convention)