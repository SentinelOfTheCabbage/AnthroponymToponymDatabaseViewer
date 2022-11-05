import os
from flask import Flask, render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate

from src.configs.constants import *
from src.db import *
from src import app, db

migrate = Migrate(app, db)

admin = Admin(app, name='Admin panel', template_mode='bootstrap4')

admin.add_view(
    ModelView(Anthroponym, db.session, category=Cat.ANTHROPONYM, name=AnthTables.ANTHROPONYM))
admin.add_view(
    AnthroponymImageModelView(AnthroponymImage, db.session, category=Cat.ANTHROPONYM, name=AnthTables.IMAGE))
admin.add_view(
    AnthroponymReferenceModelView(AnthroponymReference, db.session, category=Cat.ANTHROPONYM, name=AnthTables.REFERENCE))

admin.add_view(
    ModelView(Toponym, db.session, category=Cat.TOPONYM, name=ToponTables.TOPONYM))
admin.add_view(
    ToponymImageModelView(ToponymImage, db.session, category=Cat.TOPONYM, name=ToponTables.IMAGE))
admin.add_view(
    ModelView(ToponymReference, db.session, category=Cat.TOPONYM, name=ToponTables.REFERENCE))

admin.add_view(
    ModelView(Literature, db.session, category=Cat.OTHER, name='Литература'))


@app.route('/')
def main_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.secret_key = 'debug'
    app.run(debug=True)
