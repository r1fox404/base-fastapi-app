from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase

from core.settings import settings


class Base():
    __abstract__ = True
    
    metadata = MetaData(
        naming_convention=settings.naming_convention
    )