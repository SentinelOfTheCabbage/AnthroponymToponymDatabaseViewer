from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import VARCHAR, BIGINT, NUMERIC, JSON
from sqlalchemy.orm import relationship
from .base_model import BaseModel


class ToponymReference(BaseModel):
    __tablename__ = 'toponym_reference'
    literature_id = Column(BIGINT, ForeignKey('literature.literature_id'), nullable=False)
    toponym_id = Column(BIGINT, ForeignKey('toponym.toponym_id'), nullable=False)
    pages = Column(JSON, nullable=False)

    __mapper_args__ = {
        "primary_key": [literature_id, toponym_id]
    }
