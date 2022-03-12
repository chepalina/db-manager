from typing import Any

from fastapi import APIRouter, Depends, status

from app import dependencies
from app.api.schemas.schema_entity import SchemaEntitySchema

EVENT_TAG = "schemas"
EVENTS_PREFIX = f"/{EVENT_TAG}"

router = APIRouter(prefix=EVENTS_PREFIX, tags=[EVENT_TAG])


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[SchemaEntitySchema])
async def get_event(
    session=Depends(dependencies.get_session),
) -> Any:
    """Получить event"""
    return [SchemaEntitySchema(id=1, name="2", owner="3")]
