from flask_security import Security, SQLAlchemyUserDatastore

from ..db.secured_view import SecuredModelView, AdminModelView
from ..db.models import User, Role
from ..db.connection import db

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security()

