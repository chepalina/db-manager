from dataclasses import dataclass
from typing import TYPE_CHECKING, Type

from sqlalchemy import select

from app.models.schemas import SchemaModel
from app.services.interfaces.storage.schema_entity import SchemaEntitySchema

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio.session import AsyncSession


@dataclass
class SchemaEntityAdapter:
    session: "AsyncSession"
    model: Type[SchemaModel] = SchemaModel

    async def get_ids(self) -> list[int]:
        rows = await self.session.execute(select(SchemaModel.id))
        ids = rows.all()
        return [i[0] for i in ids]

    async def get_by_id(self, id: int) -> SchemaEntitySchema:
        rows = await self.session.execute(select(SchemaModel).where(SchemaModel.id == id))
        schema = rows.scalars().one()
        return SchemaEntitySchema.from_orm(schema)
