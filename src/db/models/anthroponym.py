from sqlalchemy.types import VARCHAR, BIGINT, NUMERIC
from sqlalchemy.orm import relationship
from sqlalchemy import CheckConstraint
from jinja2.utils import markupsafe

from ..secured_view import SecuredModelView
from ..connection import db


class Anthroponym(db.Model):
    __tablename__ = 'anthroponym'
    anthroponym_id = db.Column(BIGINT, primary_key=True)
    anthroponym = db.Column(VARCHAR(512), unique=True)
    original = db.Column(VARCHAR(512), unique=True, nullable=False)
    transcription = db.Column(VARCHAR(512), unique=True, nullable=False)
    historical_source = db.Column(VARCHAR(512), nullable=True)
    ageographical_source = db.Column(VARCHAR(512), nullable=True)
    comments = db.Column(VARCHAR(512))
    century = db.Column(NUMERIC, nullable=False)

    images = relationship("AnthroponymImage", backref='Anthroponym')
    references = relationship('AnthroponymReference', backref='Anthroponym')

    CheckConstraint(
        sqltext='historical_source IS NOT NULL or ageographical_source IS NOT NULL', 
        name='is_source_exists'
    )

    @property
    def literatures(self):
        return '\n'.join([str(ref.Literature) for ref in self.references])

    def __repr__(self):
        return f'{self.transcription} - {self.original}'


class AnthroponymModelView(SecuredModelView):
    column_searchable_list = ['anthroponym', 'original', 'transcription',
                              'historical_source', 'ageographical_source', 'century']
    column_list = ['anthroponym', 'original', 'transcription', 'historical_source',
                   'ageographical_source', 'comments', 'century', 'literatures']

    def _hist_source(view, context, model, name):
        if not model.historical_source:
            return ''
        return markupsafe.Markup(f'<i>{model.historical_source}</i>')

    def _ageograph_source(view, context, model, name):
        if not model.ageographical_source:
            return ''
        return markupsafe.Markup(f'<b>{model.ageographical_source}<b>')

    column_formatters = {
        'ageographical_source': _ageograph_source,
        'historical_source': _hist_source,
    }