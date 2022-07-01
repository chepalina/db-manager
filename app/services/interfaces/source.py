from abc import abstractmethod
from typing import Protocol



class SourceInterface(Protocol):
    @abstractmethod
    async def get_updated(self, url: str, location: str) -> str:
        pass

    @abstractmethod
    async def parse(self, id: int) -> None:
        pass

    @abstractmethod
    async def save(self, id: int) -> None:
        pass
