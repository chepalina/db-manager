from typing import Optional

from pydantic import BaseModel


class SchemaEntity(BaseModel):

    id: int
    name: str
    owner: str

    class Config:
        orm_mode = True
