from app.services.interfaces.source import SourceInterface
from dataclasses import dataclass


@dataclass
class SynchronizerService:

    source: "SourceInterface"

    def sync(self, source: SourceInterface, source_url:str, target_location: str):
        source.get_updated(source_url, target_location)
        data = source.parse()
        source.save(data)


