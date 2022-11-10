from flask_security import UserMixin, RoleMixin
from sqlalchemy.types import BIGINT, VARCHAR, INTEGER, BOOLEAN

from ..secured_view import SecuredModelView
from ..connection import db

# Flask-Security

roles_users = db.Table(
    'roles_users',
    db.Column('user_id', INTEGER, db.ForeignKey('user.id')),
    db.Column('role_id', INTEGER, db.ForeignKey('role.id'))
)


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(INTEGER, primary_key=True)
    email = db.Column(VARCHAR(100), unique=True)
    password = db.Column(VARCHAR(100))
    active = db.Column(BOOLEAN)

    roles = db.relationship(
        'Role',
        secondary=roles_users,
        backref=db.backref('users', lazy='dynamic')
    )


class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(INTEGER, primary_key=True)
    name = db.Column(VARCHAR(100), unique=True)
    description = db.Column(VARCHAR(511))

    def __repr__(self) -> str:
        return f'{self.id}: {self.name}'


class UserModelView(SecuredModelView):
    column_list = ['email', 'password', 'roles', 'active']
