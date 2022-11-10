from src.configs.constants import AnthTables, Cat, ToponTables

from .models import *
from .connection import db
from ..admin import SecuredModelView as ModelView

AnthroponymView = ModelView(Anthroponym, db.session, category=Cat.ANTHROPONYM, name=AnthTables.ANTHROPONYM)
AnthroponymImageView = AnthroponymImageModelView(AnthroponymImage, db.session, category=Cat.ANTHROPONYM, name=AnthTables.IMAGE)
AnthroponymReferenceView = AnthroponymReferenceModelView(AnthroponymReference, db.session, category=Cat.ANTHROPONYM, name=AnthTables.REFERENCE)

ToponymView = ModelView(Toponym, db.session, category=Cat.TOPONYM, name=ToponTables.TOPONYM)
ToponymImageView = ToponymImageModelView(ToponymImage, db.session, category=Cat.TOPONYM, name=ToponTables.IMAGE)
ToponymReferenceView = ModelView(ToponymReference, db.session, category=Cat.TOPONYM, name=ToponTables.REFERENCE)

LiteratureView = ModelView(Literature, db.session, category=Cat.OTHER, name='Литература')
