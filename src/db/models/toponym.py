from sqlalchemy.types import VARCHAR, BIGINT, NUMERIC
from sqlalchemy.orm import relationship
from jinja2.utils import markupsafe

from ..secured_view import SecuredModelView
from ..connection import db


class Toponym(db.Model):
    __tablename__ = 'toponym'
    toponym_id = db.Column(BIGINT, primary_key=True)
    toponym = db.Column(VARCHAR(512), unique=True)
    original = db.Column(VARCHAR(512), unique=True, nullable=False)
    transcription = db.Column(VARCHAR(512), unique=True, nullable=False)
    source = db.Column(VARCHAR(512), unique=True, nullable=False)
    comments = db.Column(VARCHAR(512))
    century = db.Column(NUMERIC, nullable=False)
    geopos = db.Column(VARCHAR(32), unique=False, nullable=False)

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
    column_list = ['toponym', 'original', 'transcription',
                   'source', 'comments', 'century', 'geopos', 'literatures']

    def geo_pos_formatter(view, context, model, name):
        if not model.geopos:
            return ''
        return markupsafe.Markup(
            '<a href="https://www.google.ru/maps/@{},{},13z">Show on google maps</a>'.format(
                *model.geopos.split(',')
            )
        )

    column_formatters = {
        'geopos': geo_pos_formatter
    }
