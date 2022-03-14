from typing import Optional

from pydantic import BaseModel


class SchemaEntitySchema(BaseModel):

    id: int
    name: str
    owner: str

    class Config:
        orm_mode = True
