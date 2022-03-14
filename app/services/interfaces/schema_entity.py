from abc import abstractmethod
from typing import Protocol

from app.services.schemas.schema_entity import SchemaEntitySchema


class SchemaEntityInterface(Protocol):
    @abstractmethod
    async def get_ids(self) -> list[int]:
        pass

    @abstractmethod
    async def get_by_id(self, id: int) -> SchemaEntitySchema:
        pass
