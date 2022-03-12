from fastapi import FastAPI

from app.api.v1.routers import schemas
from app.settings.app import AppSettings

APP_SETTINGS = AppSettings()
API_V1_PREFIX = "/api/v1"


api_v1 = FastAPI(
    title=f"{APP_SETTINGS.tag}_{APP_SETTINGS.env}",
    version=APP_SETTINGS.version,
    docs_url="/",
    redoc_url=None,
)

api_v1.include_router(schemas.router)
