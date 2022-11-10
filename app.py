import os
from flask import render_template, redirect
from flask_admin import Admin
from flask_migrate import Migrate
from flask_security import Security, SQLAlchemyUserDatastore, current_user

from src.configs.constants import *
from src.db import *
from src import app, db, security, user_datastore

db.init_app(app)
migrate = Migrate(app, db)
security.init_app(app, user_datastore)

admin = Admin(app, name='Admin panel', template_mode='bootstrap4', base_template='admin/index.html')
admin.add_view(AnthroponymView)
admin.add_view(AnthroponymImageView)
admin.add_view(AnthroponymReferenceView)

admin.add_view(ToponymView)
admin.add_view(ToponymImageView)
admin.add_view(ToponymReferenceView)

admin.add_view(LiteratureView)


### Flask-Security ###
# @app.before_first_request
# def create_user():
#     user_datastore.create_user(email='admin@mypage.ru', password='password')
#     db.session.commit()

@app.route('/')
def main_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
