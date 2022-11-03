from sqlalchemy.schema import Column
from sqlalchemy.types import VARCHAR, BIGINT, SMALLINT
from sqlalchemy.orm import relationship
from .base_model import BaseModel


class Literature(BaseModel):
    __tablename__ = 'literature'
    literature_id = Column(BIGINT, primary_key=True, nullable=False, unique=True)
    author = Column(VARCHAR, nullable=False, unique=True)
    title = Column(VARCHAR, nullable=False, unique=True)
    published_at = Column(SMALLINT, nullable=False, unique=True)

    anthroponyms = relationship('AnthroponymReference', backref='Literature')
    # toponyms = relationship('ToponymReference', backref='Literature')
