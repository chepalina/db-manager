from typing import Optional

from pydantic import BaseModel


class SchemaEntitySchema(BaseModel):

    id: Optional[int]
    name: Optional[str]
    owner: Optional[str]
