# in-module
from .types import BasicProduct, ExemptProduct


class Book(ExemptProduct):
    pass


class Food(ExemptProduct):
    pass


class Medical(ExemptProduct):
    pass


class Basic(BasicProduct):
    pass
