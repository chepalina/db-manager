from fastapi import FastAPI

from app.api.routers.system import router as system_router
from app.api.v1.registration import API_V1_PREFIX, api_v1
from app.settings.app import AppSettings

APP_SETTINGS = AppSettings()


app = FastAPI(
    title=f"{APP_SETTINGS.tag}_{APP_SETTINGS.env}",
    version=APP_SETTINGS.version,
    docs_url="/",
    redoc_url=None,
)


# @app.on_event("startup")
# async def startup_event() -> None:
#     async_engine_singleton()

# Подключение системного роутера
app.include_router(system_router)

# Подключение версий API
app.mount(API_V1_PREFIX, api_v1)
