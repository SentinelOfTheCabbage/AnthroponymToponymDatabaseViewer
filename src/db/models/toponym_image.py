from sqlalchemy.types import BIGINT, VARCHAR
from flask_admin import form
from flask import url_for
from jinja2.utils import markupsafe
import random
import os

from ..secured_view import SecuredModelView
from ..connection import db


class ToponymImage(db.Model):
    __tablename__ = 'toponym_image'
    toponym_id = db.Column(BIGINT, db.ForeignKey('toponym.toponym_id'))
    img = db.Column(VARCHAR(50), nullable=False)

    __mapper_args__ = {
        "primary_key": [toponym_id, img]
    }

class ToponymImageModelView(SecuredModelView):
    column_list = ['Anthroponym', 'img']

    def _list_thumbnail(view, context, model, name):
        if not model.img:
            return ''
        return markupsafe.Markup(
            '<img src="%s">' %
            url_for('static', filename=model.img)
        )
        # TODO: is url_for works with images?
        return "TODO"

    column_formatters = {
        'img': _list_thumbnail
    }
    form_widget_args = {
        'img': {
            'readonly': True
        },
    }
    form_extra_fields = {
        'img_file': form.FileUploadField('Image file', allowed_extensions=['jpg', 'png', 'jpeg', 'svg', 'gif'], base_path='C:\\Users\\Tom\\Documents\\programming\\Python_projects\\database_viewer\\static')
    }

    form_excluded_columns = ['img']

    def _change_img_data(self, _form):
        storage_file = _form.img_file.data

        if storage_file is not None:
            hash = random.getrandbits(32)
            ext = storage_file.filename.split('.')[-1]
            path = '%s.%s' % (hash, ext)
            while os.path.isfile(os.path.join(os.environ['IMG_STORAGE'], path)):
                hash = random.getrandbits(32)
                path = '%s.%s' % (hash, ext)
            storage_file.save(os.path.join(os.environ['IMG_STORAGE'], path))
            print(dir(_form))
            _form.img.data = path

            del _form.file

        return _form

    def edit_form(self, obj=None):
        return self._change_img_data(
            super(ToponymImageModelView, self).edit_form(obj)
        )

    def create_form(self, obj=None):
        return self._change_img_data(
            super(ToponymImageModelView, self).create_form(obj)
        )
