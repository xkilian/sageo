from .filter import Filter
from sqlalchemy import *
from sqlalchemy.orm import *

class FilterNagiosExpr(Filter):
    def __init__(self, name, title, descr, pos_filter, neg_filter, default, column_names):
        Filter.__init__(self, name, title, descr)
        self.pos_filter = pos_filter
        self.neg_filter = neg_filter
        self.default = default
        self.column_names = column_names

    def filter(self, value):
        if value == 'yes':
            return self.pos_filter 
        else:
            return self.neg_filter 

    def get_col_def(self):
        return [Column(self.name, Enum('yes', 'no', 'ignore'), default=self.default)]

