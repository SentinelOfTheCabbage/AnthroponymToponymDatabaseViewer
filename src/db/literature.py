from sqlalchemy.schema import Column
from sqlalchemy.types import VARCHAR, BIGINT, SMALLINT
from sqlalchemy.orm import relationship
from .connection import db


class Literature(db.Model):
    __tablename__ = 'literature'
    literature_id = db.Column(BIGINT, primary_key=True, nullable=False, unique=True)
    author = db.Column(VARCHAR(512),nullable=False, unique=True)
    title = db.Column(VARCHAR(512),nullable=False, unique=True)
    published_at = db.Column(SMALLINT, nullable=False, unique=True)

    anthroponyms = relationship('AnthroponymReference', backref='Literature')
    toponyms = relationship('ToponymReference', backref='Literature')

    def __repr__(self):
        return f'Литература: {self.author} - {self.title}'