from sqlalchemy.schema import Column
from sqlalchemy.types import VARCHAR, BIGINT, NUMERIC
from sqlalchemy.orm import relationship
from .base_model import BaseModel


class Anthroponym(BaseModel):
    __tablename__ = 'anthroponym'
    anthroponym_id = Column(BIGINT, primary_key=True)
    anthroponym = Column(VARCHAR, unique=True)
    original = Column(VARCHAR, unique=True, nullable=False)
    transcription = Column(VARCHAR, unique=True, nullable=False)
    source = Column(VARCHAR, unique=True, nullable=False)
    comments = Column(VARCHAR)
    century = Column(NUMERIC, nullable=False)

    images = relationship("AnthroponymImage", backref='Anthroponym')
    references = relationship('AnthroponymReference', backref='Anthroponym')
