from pydantic import BaseModel
from app.services.entities.schema import SchemaEntity


class EntitiesAggregate(BaseModel):

    schemas: list[SchemaEntity]
