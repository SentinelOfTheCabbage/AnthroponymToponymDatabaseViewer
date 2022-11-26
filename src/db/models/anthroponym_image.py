import os
import random

from flask_admin import form
from flask import url_for
from jinja2.utils import markupsafe
from sqlalchemy.types import BIGINT, VARCHAR


from ..secured_view import SecuredModelView
from ..connection import db


class AnthroponymImage(db.Model):
    __tablename__ = 'anthroponym_image'
    anthroponym_id = db.Column(BIGINT, db.ForeignKey('anthroponym.anthroponym_id'))
    img = db.Column(VARCHAR(50))

    __mapper_args__ = {
        "primary_key": [anthroponym_id, img]
    }


class AnthroponymImageModelView(SecuredModelView):
    column_list = ['Anthroponym', 'img']

    def _img_displayer(view, context, model, name):
        if not model.img:
            return ''
        return markupsafe.Markup(
            '<img src="%s" width="150">' %
            url_for('static', filename=model.img)
        )
        # TODO: is url_for works with images?
        return "TODO"

    column_formatters = {
        'img': _img_displayer
    }
    form_widget_args = {
        'img': {
            'readonly': True
        },
    }
    form_extra_fields = {
        'img_file': form.FileUploadField('Image file', allowed_extensions=['jpg', 'png', 'jpeg', 'svg', 'gif'], relative_path='./src/static/')
    }


    def _change_img_data(self, _form):
        storage_file = _form.img_file.data

        if storage_file is not None:
            hash = random.getrandbits(32)
            ext = storage_file.filename.split('.')[-1]
            path = '%s.%s' % (hash, ext)
            while os.path.isfile(os.path.join(os.environ['IMG_STORAGE'], path)):
                hash = random.getrandbits(32)
                path = '%s.%s' % (hash, ext)
            
            with open(os.path.join(os.environ['IMG_STORAGE'], path), 'wb') as gate:
                storage_file.save(gate)
            print(_form.data.items())

            _form.img = path
            self.img = path

            del _form.img_file

        return _form

    def on_model_change(self, _form, model, is_created):
        print(dir(_form))
        print(dir(model))
        print(dir(is_created))
        storage_file = model.img_file.data

        if storage_file is not None:
            hash = random.getrandbits(32)
            ext = storage_file.filename.split('.')[-1]
            path = '%s.%s' % (hash, ext)
            while os.path.isfile(os.path.join(os.environ['IMG_STORAGE'], path)):
                hash = random.getrandbits(32)
                path = '%s.%s' % (hash, ext)
            
            with open(os.path.join(os.environ['IMG_STORAGE'], path), 'wb') as gate:
                storage_file.save(gate)

            _form.img = path
            self.img = path
            model.img = path

            del _form.img_file

        return _form

    def edit_form(self, obj=None):
        return self._change_img_data(
            super(AnthroponymImageModelView, self).edit_form(obj)
        )

    def create_form(self, obj=None):
        return self._change_img_data(
            super(AnthroponymImageModelView, self).create_form(obj)
        )
