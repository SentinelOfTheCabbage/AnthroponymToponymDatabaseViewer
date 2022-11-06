from flask_admin.contrib.sqla import ModelView
from src.configs.constants import AnthTables, Cat, ToponTables

from .models.anthroponym import Anthroponym
from .models.anthroponym_image import AnthroponymImage, AnthroponymImageModelView
from .models.anthroponym_reference import AnthroponymReference, AnthroponymReferenceModelView
from .models.literature import Literature
from .models.toponym import Toponym
from .models.toponym_image import ToponymImage, ToponymImageModelView
from .models.toponym_reference import ToponymReference
from .models.roles import Role, User, roles_users
from .connection import db

AnthroponymView = ModelView(Anthroponym, db.session, category=Cat.ANTHROPONYM, name=AnthTables.ANTHROPONYM)
AnthroponymImageView = AnthroponymImageModelView(AnthroponymImage, db.session, category=Cat.ANTHROPONYM, name=AnthTables.IMAGE)
AnthroponymReferenceView = AnthroponymReferenceModelView(AnthroponymReference, db.session, category=Cat.ANTHROPONYM, name=AnthTables.REFERENCE)

ToponymView = ModelView(Toponym, db.session, category=Cat.TOPONYM, name=ToponTables.TOPONYM)
ToponymImageView = ToponymImageModelView(ToponymImage, db.session, category=Cat.TOPONYM, name=ToponTables.IMAGE)
ToponymReferenceView = ModelView(ToponymReference, db.session, category=Cat.TOPONYM, name=ToponTables.REFERENCE)

LiteratureView = ModelView(Literature, db.session, category=Cat.OTHER, name='Литература')
