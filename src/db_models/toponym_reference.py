from sqlalchemy.schema import Column
from sqlalchemy.types import VARCHAR, BIGINT, NUMERIC, JSON
from sqlalchemy.orm import relationship, ForeignKey
from db_models.base_model import BaseModel


class ToponymReference(BaseModel):
    __tablename__ = 'toponym_reference'
    toponym_id = Column(BIGINT, ForeignKey('toroponym.toponym_id'), nullable=False)
    literature_id = Column(BIGINT, ForeignKey('literature.literature_id'), nullable=False)
    pages = Column(JSON, nullable=False)
