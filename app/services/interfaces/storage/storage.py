from abc import abstractmethod
from typing import Protocol

from app.services.aggregates.entities import EntitiesAggregate


class StorageInterface(Protocol):

    @abstractmethod
    async def save_config(self, entities: EntitiesAggregate) -> None:
        pass
