from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import BIGINT, JSON
from sqlalchemy.orm import relationship
from db_models.base_model import BaseModel


class AnthroponymReference(BaseModel):
    __tablename__ = 'anthroponym_reference'
    literature_id = Column(BIGINT, ForeignKey('literature.literature_id'), nullable=False)
    anthroponym_id = Column(BIGINT, ForeignKey('anthroponym.anthroponym_id'), nullable=False)
    pages = Column(JSON, nullable=False)
    
    __mapper_args__ = {
        "primary_key": [literature_id, anthroponym_id]
    }
