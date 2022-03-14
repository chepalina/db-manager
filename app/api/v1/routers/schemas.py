from typing import Any

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncEngine

from app import dependencies
from app.crud.schema_entity import SchemaEntityCRUD
from app.services.schemas.schema_entity import SchemaEntitySchema

EVENT_TAG = "schemas"
EVENTS_PREFIX = f"/{EVENT_TAG}"

router = APIRouter(prefix=EVENTS_PREFIX, tags=[EVENT_TAG])


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[int])
async def get(
    db: AsyncEngine = Depends(dependencies.get_session),
) -> Any:
    """Get schemas."""
    return await SchemaEntityCRUD(db).get_ids()


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=SchemaEntitySchema)
async def get_by_id(
    id: int,
    db: AsyncEngine = Depends(dependencies.get_session),
) -> Any:
    """Get schema by id."""
    return await SchemaEntityCRUD(db).get_by_id(id)
