from sqlalchemy.schema import Column
from sqlalchemy.types import VARCHAR, BIGINT, NUMERIC
from sqlalchemy.orm import relationship
from db_models.base_model import BaseModel


class Toponym(BaseModel):
    __tablename__ = 'toponym'
    toponym_id = Column(BIGINT, primary_key=True)
    toponym = Column(VARCHAR, unique=True)
    original = Column(VARCHAR, unique=True, nullable=False)
    transcription = Column(VARCHAR, unique =True, nullable=False)
    source = Column(VARCHAR, unique=True, nullable=False)
    comments = Column(VARCHAR)
    century = Column(NUMERIC, nullable=False)

    images = relationship("toponym_image")
    references = relationship('toponym_reference')
