from sqlalchemy.types import BIGINT, BLOB
from flask_admin import form
import random
import os

from ..secured_view import SecuredModelView
from ..connection import db


class ToponymImage(db.Model):
    __tablename__ = 'toponym_image'
    toponym_id = db.Column(BIGINT, db.ForeignKey('toponym.toponym_id'))
    img = db.Column(BLOB)

    __mapper_args__ = {
        "primary_key": [toponym_id, img]
    }

class ToponymImageModelView(SecuredModelView):
    column_list = ['Troponym', 'Image file']

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
            super(ToponymImageModelView, self).edit_form(obj)
        )

    def create_form(self, obj=None):
        return self._change_img_data(
            super(ToponymImageModelView, self).create_form(obj)
        )
