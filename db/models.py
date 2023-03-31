from datetime import datetime

import marshmallow.fields as ma_fields
from marshmallow import Schema
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, JSON, DateTime

Base = declarative_base()


class Example(Base):
    __tablename__ = "examples"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=True)
    data = Column(JSON(), nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


class ExampleResponseSchema(Schema):
    id = ma_fields.Integer()
    name = ma_fields.String()
    data = ma_fields.Dict()

    created_at = ma_fields.DateTime()
    updated_at = ma_fields.DateTime()
