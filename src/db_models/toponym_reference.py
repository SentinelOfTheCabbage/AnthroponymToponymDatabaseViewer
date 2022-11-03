from sqlalchemy.schema import Column
from sqlalchemy.types import VARCHAR, BIGINT, NUMERIC, JSON
from sqlalchemy.orm import relationship, ForeignKey
from .base_model import BaseModel


class ToponymReference(BaseModel):
    __tablename__ = 'toponym_reference'
    literature_id = Column(BIGINT, ForeignKey('literature.literature_id'), nullable=False)
    pages = Column(JSON, nullable=False)
