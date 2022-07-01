from pydantic import BaseModel, AnyHttpUrl
from utils.base_dir import INSTANCE_DIR


class GitSettings(BaseModel):
    """Класс настройки подключения к git."""

    repo_name: str = "db-config"
    url: AnyHttpUrl = f"https://github.com/polinamasl/{repo_name}.git"
    local: str = f"{INSTANCE_DIR}/repo"

    class Config:
        env_prefix = "git_"
