from sqlalchemy.schema import Column
from sqlalchemy.types import VARCHAR, BIGINT, NUMERIC
from sqlalchemy.orm import relationship
from .connection import db


class Toponym(db.Model):
    __tablename__ = 'toponym'
    toponym_id = db.Column(BIGINT, primary_key=True)
    toponym = db.Column(VARCHAR(512),unique=True)
    original = db.Column(VARCHAR(512),unique=True, nullable=False)
    transcription = db.Column(VARCHAR(512),unique =True, nullable=False)
    source = db.Column(VARCHAR(512),unique=True, nullable=False)
    comments = db.Column(VARCHAR(512))
    century = db.Column(NUMERIC, nullable=False)

    images = relationship("ToponymImage", backref='Toponym')
    references = relationship('ToponymReference', backref='Toponym')
