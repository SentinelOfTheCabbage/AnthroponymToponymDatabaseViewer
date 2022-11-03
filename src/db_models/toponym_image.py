from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import VARCHAR, BIGINT, NUMERIC, BLOB
from sqlalchemy.orm import relationship
from db_models.base_model import BaseModel


class ToponymImage(BaseModel):
    __tablename__ = 'toponym_image'
    anthroponym_id = Column(BIGINT, ForeignKey('toponym.toponym_id'))
    img = Column(BLOB)
