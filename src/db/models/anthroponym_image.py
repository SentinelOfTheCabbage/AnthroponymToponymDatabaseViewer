import os
import random

from sqlalchemy.types import BIGINT, BLOB
from flask_admin import form

from ..secured_view import SecuredModelView
from ..connection import db


class AnthroponymImage(db.Model):
    __tablename__ = 'anthroponym_image'
    anthroponym_id = db.Column(BIGINT, db.ForeignKey('anthroponym.anthroponym_id'))
    img = db.Column(BLOB)

    __mapper_args__ = {
        "primary_key": [anthroponym_id, img]
    }


class AnthroponymImageModelView(SecuredModelView):
    column_list = ['Anthroponym', 'Image file']

    def _list_thumbnail(view, context, model, name):
        # TODO: how to display it on view page?
        return "TODO"


    column_formatters = {
        'img': _list_thumbnail
    }

    form_extra_fields = {
        'img_file': form.FileUploadField('Image file', allowed_extensions=['jpg','png','jpeg', 'svg', 'gif'])
    }

    form_excluded_columns = ['img']
    def _change_img_data(self, _form):
        try:
            storage_file = _form.img_file.data

            if storage_file is not None:
                hash = random.getrandbits(128)
                ext = storage_file.filename.split('.')[-1]
                path = '%s.%s' % (hash, ext)
                # TODO: change img field type to VARCHAR ?
                storage_file.save(
                    os.path.join(os.environ['IMG_STORAGE'], path)
                )

                del _form.file

        except Exception as ex:
            pass

        return _form

    def edit_form(self, obj=None):
        return self._change_img_data(
            super(AnthroponymImageModelView, self).edit_form(obj)
        )

    def create_form(self, obj=None):
        return self._change_img_data(
            super(AnthroponymImageModelView, self).create_form(obj)
        )
