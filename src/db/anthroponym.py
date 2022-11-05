from sqlalchemy.schema import Column
from sqlalchemy.types import VARCHAR, BIGINT, NUMERIC
from sqlalchemy.orm import relationship
from .connection import db


class Anthroponym(db.Model):
    __tablename__ = 'anthroponym'
    anthroponym_id = db.Column(BIGINT, primary_key=True)
    anthroponym = db.Column(VARCHAR(512),unique=True)
    original = db.Column(VARCHAR(512),unique=True, nullable=False)
    transcription = db.Column(VARCHAR(512),unique=True, nullable=False)
    source = db.Column(VARCHAR(512),unique=True, nullable=False)
    comments = db.Column(VARCHAR(512))
    century = db.Column(NUMERIC, nullable=False)

    images = relationship("AnthroponymImage", backref='Anthroponym')
    references = relationship('AnthroponymReference', backref='Anthroponym')

    def __repr__(self):
        return f'Антропоним: {self.anthroponym} - {self.original} - {self.transcription}'