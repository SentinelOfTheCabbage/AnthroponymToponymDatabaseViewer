import os
from flask import render_template
from flask_admin import Admin
from flask_migrate import Migrate
from src.configs.constants import *
from src.db import *
from src import app, db, security, user_datastore

db.init_app(app)
migrate = Migrate(app, db)
security.init_app(app, user_datastore)

admin = Admin(app, name='Антропонимус', template_mode='bootstrap4')
admin.add_view(AnthroponymView)
admin.add_view(AnthroponymImageView)
admin.add_view(AnthroponymReferenceView)

admin.add_view(ToponymView)
admin.add_view(ToponymImageView)
admin.add_view(ToponymReferenceView)

admin.add_view(LiteratureView)

admin.add_view(UsersView)
admin.add_view(RolesView)
# admin.add_view(UserRoles)

### Flask-Security init code ###
# @app.before_first_request
# def create_user():
#     user_datastore.create_role(name='moderator', description='Can watch only part of tables. Can\' edit them')
#     moderator_role = user_datastore.find_role('moderator')
#     user_datastore.create_user(email='moderator', password='password', roles=[moderator_role])
#     db.session.commit()
#     user_datastore.create_role(name='admin', description='Can add other users. Can see and edit any table')
#     admin_role = user_datastore.find_role('admin')
#     user_datastore.create_user(email='admin', password='password', roles=[admin_role])
#     db.session.commit()

@app.route('/')
def main_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
