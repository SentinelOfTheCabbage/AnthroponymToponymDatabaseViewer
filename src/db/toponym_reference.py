from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import BIGINT, JSON
from .connection import db


class ToponymReference(db.Model):
    __tablename__ = 'toponym_reference'
    literature_id = db.Column(BIGINT, ForeignKey('literature.literature_id'), nullable=False)
    toponym_id = db.Column(BIGINT, ForeignKey('toponym.toponym_id'), nullable=False)
    pages = db.Column(JSON, nullable=False)

    __mapper_args__ = {
        "primary_key": [literature_id, toponym_id]
    }
