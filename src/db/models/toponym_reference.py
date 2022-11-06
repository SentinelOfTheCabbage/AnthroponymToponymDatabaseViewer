from sqlalchemy.types import BIGINT, VARCHAR
from ..connection import db


class ToponymReference(db.Model):
    __tablename__ = 'toponym_reference'
    literature_id = db.Column(BIGINT, db.ForeignKey('literature.literature_id'), nullable=False)
    toponym_id = db.Column(BIGINT, db.ForeignKey('toponym.toponym_id'), nullable=False)
    pages = db.Column(VARCHAR(100), nullable=False)

    __mapper_args__ = {
        "primary_key": [literature_id, toponym_id]
    }