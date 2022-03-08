from http import HTTPStatus

from fastapi import APIRouter, Response

SYSTEM_TAG = "system"
SYSTEM_PREFIX = f"/{SYSTEM_TAG}"

router = APIRouter(prefix=SYSTEM_PREFIX, tags=[SYSTEM_TAG])


@router.get(
    "/liveness",
    status_code=HTTPStatus.NO_CONTENT,
    response_class=Response,
    responses={
        HTTPStatus.NO_CONTENT.value: {"description": HTTPStatus.NO_CONTENT.phrase},
    },
)
async def liveness() -> None:
    """Проверка доступности сервиса."""
    return None


@router.get(
    "/readiness",
    status_code=HTTPStatus.NO_CONTENT,
    response_class=Response,
    responses={
        HTTPStatus.NO_CONTENT.value: {"description": HTTPStatus.NO_CONTENT.phrase},
        HTTPStatus.SERVICE_UNAVAILABLE.value: {
            "description": HTTPStatus.SERVICE_UNAVAILABLE.phrase
        },
    },
)
async def readiness() -> None:
    """Проверка готовности сервиса."""
    return None
