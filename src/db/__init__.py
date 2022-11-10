from src.configs.constants import AnthTables, Cat, ToponTables, UsersNRoles

from .models import *
from .connection import db
from ..admin import SecuredModelView, AdminModelView

AnthroponymView = SecuredModelView(Anthroponym, db.session, category=Cat.ANTHROPONYM, name=AnthTables.ANTHROPONYM)
AnthroponymImageView = AnthroponymImageModelView(AnthroponymImage, db.session, category=Cat.ANTHROPONYM, name=AnthTables.IMAGE)
AnthroponymReferenceView = AnthroponymReferenceModelView(AnthroponymReference, db.session, category=Cat.ANTHROPONYM, name=AnthTables.REFERENCE)

ToponymView = SecuredModelView(Toponym, db.session, category=Cat.TOPONYM, name=ToponTables.TOPONYM)
ToponymImageView = ToponymImageModelView(ToponymImage, db.session, category=Cat.TOPONYM, name=ToponTables.IMAGE)
ToponymReferenceView = SecuredModelView(ToponymReference, db.session, category=Cat.TOPONYM, name=ToponTables.REFERENCE)

LiteratureView = SecuredModelView(Literature, db.session, category=Cat.OTHER, name='Литература')

UsersView = UserModelView(User, db.session, category=Cat.USERS, name=UsersNRoles.USER)
RolesView = AdminModelView(Role, db.session, category=Cat.USERS, name=UsersNRoles.ROLE)
# UserRoles = AdminModelView(roles_users, db.session, category=Cat.USERS, name=UsersNRoles.USERSROLE)