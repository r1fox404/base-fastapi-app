from fastapi import APIRouter

from application.core.settings import settings
from .views.users import router as users_router

router = APIRouter(prefix=settings.api.v1.prefix)
router.include_router(users_router, prefix=settings.api.v1.users)