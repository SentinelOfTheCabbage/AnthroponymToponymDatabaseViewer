from flask_admin.contrib.sqla import ModelView
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import BIGINT, BLOB
from .connection import db


class AnthroponymImage(db.Model):
    __tablename__ = 'anthroponym_image'
    anthroponym_id = db.Column(BIGINT, ForeignKey('anthroponym.anthroponym_id'))
    img = db.Column(BLOB)

    __mapper_args__ = {
        "primary_key": [anthroponym_id, img]
    }


class AnthroponymImageModelView(ModelView):
    # TODO: make file uploading page!
    create_template = 'create_anthroponym_image.html'
