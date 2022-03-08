from fastapi import FastAPI

from app.api.routers.system import router as system_router
from app.api.v1.registration import API_V1_PREFIX, api_v1
from app.db import async_engine_singleton
from app.settings.app import AppSettings
from utils.settings.validator import validate_settings

APP_SETTINGS = AppSettings()


app = FastAPI(
    title=f"{APP_SETTINGS.tag}_{APP_SETTINGS.env}",
    version=APP_SETTINGS.version,
    docs_url="/",
    redoc_url=None,
)


@app.on_event("startup")
async def startup_event() -> None:
    """Инициализация зависимостей приложения перед запуском."""
    # Провалидировать все настройки
    validate_settings("app.settings")
    async_engine_singleton()

# Подключение системного роутера
app.include_router(system_router)

# Подключение версий API
app.mount(API_V1_PREFIX, api_v1)
