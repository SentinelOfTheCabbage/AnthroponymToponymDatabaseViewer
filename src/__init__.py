import os
from flask import Flask

from .db import db
from .admin import security, user_datastore

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SECURITY_PASSWORD_SALT'] = 'HELLO WORLD'
app.config['SECURITY_PASSWORD_HASH'] = 'bcrypt'
app.config['SECURITY_POST_LOGIN_VIEW'] = '/admin'
app.config['SECURITY_POST_LOGOUT_VIEW'] = '/login'
