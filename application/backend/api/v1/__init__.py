from fastapi import APIRouter

from application.core.settings import settings
from .views.users import router as users_router
from .views.events import router as events_router
from .views.contracts import router as contracts_router

router = APIRouter(prefix=settings.api.v1.prefix)
router.include_router(users_router, prefix=settings.api.v1.users)
router.include_router(events_router, prefix=settings.api.v1.events)
router.include_router(contracts_router, prefix=settings.api.v1.contracts)