# internal
from .item import Item

# 1st party
from product.core import Product

# 3rd party
from typing import List


class Receipt:
    items = []              # type: List[Item]
    # automatic values
    total_tax_amount = 0.0  # type: float
    total_cost = 0.0        # type: float

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
