from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import VARCHAR, BIGINT, NUMERIC, BLOB
from sqlalchemy.orm import relationship
from .base_model import BaseModel


class ToponymImage(BaseModel):
    __tablename__ = 'toponym_image'
    toponym_id = Column(BIGINT, ForeignKey('toponym.toponym_id'))
    img = Column(BLOB)

    __mapper_args__ = {
        "primary_key": [toponym_id, img]
    }
