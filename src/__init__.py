import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .db import db

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
db.init_app(app)