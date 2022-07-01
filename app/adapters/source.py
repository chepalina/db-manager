from app.services.interfaces.source import SourceInterface
from git import Repo
import os
import yaml

class SourceAdapter(SourceInterface):

    async def get_updated(self, url: str, location: str) -> str:
        if os.path.exists(location):
            # repo = Git(location).pull
            pass
        Repo.clone_from(url, location)
        return "1"

    async def parse(self, location: str) -> None:
        with location.open("r") as config_file:
            data = yaml.load(config_file, yaml.Loader)

    async def save(self, id: int) -> None:
        pass


import asyncio
from app.settings.git import GitSettings


s = GitSettings()
x = SourceAdapter()
asyncio.run(x.get_updated(s.url, s.local))
