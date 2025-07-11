import uvicorn

from fastapi import FastAPI

from application.backend.api.v1 import router
from application.core.settings import settings

main_app = FastAPI()
main_app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(
        main_app,
        host=settings.run.host,
        port=settings.run.port)