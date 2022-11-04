from enum import Enum
from flask import Flask, render_template, url_for
from flask_admin import Admin

from flask_admin.contrib.sqla import ModelView

# from db_models import View

from .db_models import db_session
from .db_models import Anthroponym, AnthroponymImage, AnthroponymReference
from .db_models import Toponym, ToponymImage, ToponymReference
from .db_models import Literature

app = Flask(__name__)


class MetaEnum(str, Enum):
    def __str__(self):
        return self.value


class Categories(MetaEnum):
    ANTHROPONYM = 'Антропонимы'
    TOPONYM = 'Топоним'
    OTHER = 'Остальное'


class AnthroponymTables(MetaEnum):
    ANTHROPONYM = 'Антропонимы'
    IMAGE = 'Изображения'
    REFERENCE = 'Референсы'


class ToponymTables(MetaEnum):
    TOPONYM = 'Топонимы'
    IMAGE = 'Изображения'
    REFERENCE = 'Референсы'


admin = Admin(app, name='Admin panel', template_mode='bootstrap4')

admin.add_view(ModelView(Anthroponym, db_session, category=Categories.ANTHROPONYM, name=AnthroponymTables.ANTHROPONYM))
admin.add_view(ModelView(AnthroponymImage, db_session, category=Categories.ANTHROPONYM, name=AnthroponymTables.IMAGE))
admin.add_view(ModelView(AnthroponymReference, db_session, category=Categories.ANTHROPONYM, name=AnthroponymTables.REFERENCE))

admin.add_view(ModelView(Toponym, db_session, category=Categories.TOPONYM, name=ToponymTables.TOPONYM))
admin.add_view(ModelView(ToponymImage, db_session, category=Categories.TOPONYM, name=ToponymTables.IMAGE))
admin.add_view(ModelView(ToponymReference, db_session, category=Categories.TOPONYM, name=ToponymTables.REFERENCE))

admin.add_view(ModelView(Literature, db_session, category=Categories.OTHER, name='Литература'))


@app.route('/')
def main_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.secret_key = 'debug'
    app.run(debug=True)
