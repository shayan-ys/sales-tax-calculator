# internal
from .item import Item

# 1st party
from product.core import Product
from product.categories import category_identifier, category_class_by_name
import constant

# 3rd party
from typing import List, Tuple


class Receipt:
    items = []              # type: List[Item]
    # automatic values
    total_tax_amount = 0.0  # type: float
    total_cost = 0.0        # type: float

    def __init__(self):
        self.items = []
        self.total_tax_amount = 0.0
        self.total_cost = 0.0

    def add(self, product: Product, count: int = 1):
        """Add product to list of receipt items
        Update total tax and total cost

        Example:
            book = Book(10.0)
            receipt.add(book, 2)
            receipt.total_tax_amount = 0
            receipt.total_cost = 10.0
        """
        item = Item(product, count=count)
        self.items.append(item)

        # update total tax
        total_tax = self.total_tax_amount + (product.tax_amount * count)
        self.total_tax_amount = float("{0:.2f}".format(total_tax))

        # update total cost
        total_cost = self.total_cost + (product.cost * count)
        self.total_cost = float("{0:.2f}".format(total_cost))

    def populate(self, items_data: List[Tuple]):
        """
        populate receipt using given items_data which is a list of tuples of specific type:
            (int, bool, str, float) for (count, imported/or not, product name, price)
        :param items_data:
        :return:
        """
        for count, imported, name, category_str, price in items_data:
            if category_str:
                category = category_class_by_name(category_str=category_str)
            else:
                category = category_identifier(product_title=name)
            product = category(price=price, imported=imported, name=name)
            self.add(product=product, count=count)

    def __str__(self):
        items_str = '\n'.join(map(str, self.items))
        return "{0}\n{1}: {2:.2f}\n{3}: {4:.2f}".format(
            items_str,
            constant.Strings.SALES_TAXES, self.total_tax_amount,
            constant.Strings.TOTAL, self.total_cost
        )

    def __dict__(self):
        return {
            'items': list(map(dict, self.items)),
            'total sale taxes': self.total_tax_amount,
            'total cost': self.total_cost
        }
