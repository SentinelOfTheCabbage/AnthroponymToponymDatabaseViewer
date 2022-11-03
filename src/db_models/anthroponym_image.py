from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import VARCHAR, BIGINT, NUMERIC, BLOB
from sqlalchemy.orm import relationship
from .base_model import BaseModel

class AnthroponymImage(BaseModel):
    __tablename__ = 'anthroponym_image'
    anthroponym_id = Column(BIGINT, ForeignKey('anthroponym.anthroponym_id'))
    img = Column(BLOB)