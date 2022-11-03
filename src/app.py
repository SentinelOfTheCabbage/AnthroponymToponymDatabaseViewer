from enum import Enum
from flask import Flask, render_template, url_for
from flask_admin import Admin

from flask_admin.contrib.sqla import ModelView
# from db_models import View

from db_models import db_session, CustomView
from db_models import Anthroponym, AnthroponymImage, AnthroponymReference, Literature

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

admin = Admin(app, name='Admin panel', template_mode='bootstrap3')
admin.add_view(ModelView(Anthroponym, db_session, category=Categories.ANTHROPONYM, name=AnthroponymTables.ANTHROPONYM))
admin.add_view(ModelView(AnthroponymImage, db_session, category=Categories.ANTHROPONYM, name=AnthroponymTables.IMAGE))
admin.add_view(ModelView(AnthroponymReference, db_session, category=Categories.ANTHROPONYM, name=AnthroponymTables.REFERENCE))
# admin.add_view(CustomView(AnthroponymReference, db_session, columns=['anthroponym_id', 'literature_id', 'pages']))
admin.add_view(ModelView(Literature, db_session, category=Categories.OTHER, name='Литература'))

@app.route('/')
def main_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.secret_key = 'debug'
    app.run(debug=True)
