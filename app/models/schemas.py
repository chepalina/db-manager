from sqlalchemy import Column
from sqlalchemy.orm.attributes import Mapped
from sqlalchemy.sql.sqltypes import Integer, String

from app.db import Base


class SchemaModel(Base):

    __tablename__ = "schemas"

    id: Mapped[int] = Column(Integer(), primary_key=True)
    name: Mapped[str] = Column(String(length=32))
    owner: Mapped[str] = Column(String(length=32))
