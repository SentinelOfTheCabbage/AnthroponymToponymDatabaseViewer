from flask_admin.contrib.sqla import ModelView
from sqlalchemy.types import BIGINT, BLOB
from ..connection import db


class ToponymImage(db.Model):
    __tablename__ = 'toponym_image'
    toponym_id = db.Column(BIGINT, db.ForeignKey('toponym.toponym_id'))
    img = db.Column(BLOB)

    __mapper_args__ = {
        "primary_key": [toponym_id, img]
    }

class ToponymImageModelView(ModelView):
    edit_template = 'edit_toponym_image.html'
    create_template = 'create_toponym_image.html'
