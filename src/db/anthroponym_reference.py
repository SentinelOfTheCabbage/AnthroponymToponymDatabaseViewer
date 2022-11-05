from flask_admin.contrib.sqla import ModelView
from sqlalchemy.types import BIGINT, JSON
from .connection import db


class AnthroponymReference(db.Model):
    __tablename__ = 'anthroponym_reference'
    literature_id = db.Column(BIGINT, db.ForeignKey('literature.literature_id'), nullable=False, primary_key=False)
    anthroponym_id = db.Column(BIGINT, db.ForeignKey('anthroponym.anthroponym_id'), nullable=False, primary_key=False)
    # TODO : make pages String, not JSON. Like '1, 15-22'
    pages = db.Column(JSON, nullable=False)

    __mapper_args__ = {
        "primary_key": [literature_id, anthroponym_id]
    }

class AnthroponymReferenceModelView(ModelView):
    column_list = ['Literature', 'Anthroponym', 'pages']
