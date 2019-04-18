# in-module
from .core import Product

# 1st party modules
import tax.categories


class BasicProduct(Product):
    tax_profile = tax.categories.BasicDomestic


class ExemptProduct(Product):
    tax_profile = tax.categories.ExemptDomestic
