from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView
from sqlalchemy import inspect

engine = create_engine('mysql://root:password@localhost:3306/anthroponyms_toponyms')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

BaseModel = declarative_base()

class CustomView(ModelView):
    column_display_pk = True
    column_hide_backrefs = False
    
    def __init__(self, model, session, name=None, category=None, endpoint=None, url=None, static_folder=None, menu_class_name=None, menu_icon_type=None, menu_icon_value=None, columns=[]):
        self.column_list = columns
        super().__init__(model, session, name, category, endpoint, url, static_folder, menu_class_name, menu_icon_type, menu_icon_value)

# breakpoint()