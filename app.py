import os
from flask import render_template
from flask_admin import Admin
from flask_migrate import Migrate

from src.configs.constants import *
from src.db import *
from src import app, db

migrate = Migrate(app, db)

admin = Admin(app, name='Admin panel', template_mode='bootstrap4')

admin.add_view(AnthroponymView)
admin.add_view(AnthroponymImageView)
admin.add_view(AnthroponymReferenceView)

admin.add_view(ToponymView)
admin.add_view(ToponymImageView)
admin.add_view(ToponymReferenceView)

admin.add_view(LiteratureView)


@app.route('/')
def main_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
