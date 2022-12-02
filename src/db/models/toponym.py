from sqlalchemy.types import VARCHAR, BIGINT, NUMERIC
from sqlalchemy.orm import relationship
from sqlalchemy import CheckConstraint
from jinja2.utils import markupsafe

from ..secured_view import SecuredModelView
from ..connection import db


class Toponym(db.Model):
    __tablename__ = 'toponym'
    toponym_id = db.Column(BIGINT, primary_key=True)
    toponym = db.Column(VARCHAR(512), unique=True)
    original = db.Column(VARCHAR(512), unique=True, nullable=False)
    transcription = db.Column(VARCHAR(512), unique=True, nullable=False)
    historical_source = db.Column(VARCHAR(512), nullable=True)
    ageographical_source = db.Column(VARCHAR(512), nullable=True)
    comments = db.Column(VARCHAR(512))
    century = db.Column(NUMERIC, nullable=False)
    geopos = db.Column(VARCHAR(32), unique=False, nullable=False)

    images = relationship("ToponymImage", backref='Toponym')
    references = relationship('ToponymReference', backref='Toponym')

    CheckConstraint(
        sqltext='historical_source IS NOT NULL or ageographical_source IS NOT NULL',
        name='is_source_exists'
    )

    @property
    def literatures(self):
        return '\n'.join([str(ref.Literature) for ref in self.references])

    def __repr__(self):
        return f'{self.transcription} - {self.original}'

    def __str__(self):
        return self.__repr__()


class ToponymModelView(SecuredModelView):
    column_searchable_list = ['toponym', 'original', 'transcription',
                              'historical_source', 'ageographical_source', 'century']
    column_list = ['toponym', 'original', 'transcription', 'historical_source',
                   'ageographical_source', 'comments', 'century', 'geopos', 'literatures']


    def geo_pos_formatter(view, context, model, name):
        if not model.geopos:
            return ''
        return markupsafe.Markup(
            '<a href="https://www.google.ru/maps/@{},13z">Show on google maps</a>'.format(
                model.geopos
            )
        )

    def _hist_source(view, context, model, name):
        if not model.historical_source:
            return ''
        return markupsafe.Markup(f'<b>{model.historical_source}</b>')


    def _ageograph_source(view, context, model, name):
        if not model.ageographical_source:
            return ''
        return markupsafe.Markup(f'<i>{model.ageographical_source}</i>')

    column_formatters = {
        'geopos': geo_pos_formatter,
        'ageographical_source': _ageograph_source,
        'historical_source': _hist_source,
    }
