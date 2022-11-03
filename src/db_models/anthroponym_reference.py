from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import BIGINT, JSON
from sqlalchemy.orm import relationship
from .base_model import BaseModel


class AnthroponymReference(BaseModel):
    __tablename__ = 'anthroponym_reference'
    literature_id = Column(BIGINT, ForeignKey('literature.literature_id'), nullable=False, primary_key=False)
    anthroponym_id = Column(BIGINT, ForeignKey('anthroponym.anthroponym_id'), nullable=False, primary_key=False)
    pages = Column(JSON, nullable=False)
