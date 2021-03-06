from sqlalchemy import *
from sqlalchemy.orm import *
from app.db_model.base import Base
from flask.ext.babelex import lazy_gettext, gettext, ngettext, Babel
from app import babel, app
from flask import Flask
from app.db_model.view import View
from app.model.columns.builtin import get_columns_pairs
from app.model.columns.builtin import get_columns_name
import ast
_ = lazy_gettext

column_choices = get_columns_pairs() 
column_names = get_columns_name()
if ('','') in column_choices:
    column_choices.remove(('',''))
if '' in column_names:
    column_names.remove('')
enum_col = Enum(*column_names) 

class ViewColumn(Base):
    __tablename__ = 'view_column'
    id = Column(Integer, primary_key=True)
    column = Column(enum_col, nullable=False, info={'choices':column_choices} )
    parent_id = Column(Integer, ForeignKey(View.id), nullable=False)
    view = relationship(
        View,
        backref = 'view_column'
    )
