from sqlalchemy.types import VARCHAR, BIGINT, NUMERIC
from sqlalchemy.orm import relationship

from ..secured_view import SecuredModelView
from ..connection import db


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

    @property
    def literatures(self):
        return '\n'.join([str(ref.Literature) for ref in self.references])

    def __repr__(self):
        return f'{self.transcription} - {self.original}'

    def __str__(self):
        return self.__repr__()

class ToponymModelView(SecuredModelView):
    column_searchable_list = ['toponym', 'original', 'transcription', 'source', 'century']
    column_list = ['toponym', 'original', 'transcription', 'source', 'comments', 'century', 'literatures']
