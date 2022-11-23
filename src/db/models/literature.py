from sqlalchemy.types import VARCHAR, BIGINT, SMALLINT
from sqlalchemy.orm import relationship

from ..secured_view import SecuredModelView
from ..connection import db


class Literature(db.Model):
    __tablename__ = 'literature'
    literature_id = db.Column(BIGINT, primary_key=True, nullable=False, unique=True)
    author = db.Column(VARCHAR(512),nullable=False, unique=True)
    title = db.Column(VARCHAR(512),nullable=False, unique=True)
    published_at = db.Column(SMALLINT, nullable=False, unique=True)

    anthroponyms = relationship('AnthroponymReference', backref='Literature')
    toponyms = relationship('ToponymReference', backref='Literature')

    def __repr__(self):
        return f'{self.author} - `{self.title}`'

    def __str__(self):
        return self.__repr__()

class LiteratureModelView(SecuredModelView):
    column_searchable_list = ['author', 'title']
