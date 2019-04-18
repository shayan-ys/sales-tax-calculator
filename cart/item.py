from product.core import Product


class Item:
    """Container to store multiple count of same product in the receipt
    Usage:
        cart.receipt.Receipt
    """
    product = None          # type: Product
    count = 0               # type: int
    # automated
    total_tax_amount = 0.0  # type: float
    total_cost = 0.0        # type: float

    def __init__(self, product_obj: Product, count: int):
        self.product = product_obj
        self.count = count

        # update total tax
        total_tax = product_obj.tax_amount * count
        self.total_tax_amount = float("{0:.2f}".format(total_tax))

        # update total cost
        total_cost = product_obj.cost * count
        self.total_cost = float("{0:.2f}".format(total_cost))

    def __str__(self):
        """
        Example:
            3 imported book: 37.80
        :return:
        """
        return "{0} {1}: {2:.2f}".format(self.count, str(self.product), self.total_cost)

    def __repr__(self):
        return self.__str__()

    def __dict__(self):
        """
        Example:
            {'count': 3, 'imported': True, 'product': 'imported book', 'cost': 37.8, 'tax': 1.8}
        :return:
        """
        return {
            'count': self.count,
            'imported': self.product.imported,
            'product': str(self.product),
            'cost': self.total_cost,
            'tax': self.total_tax_amount
        }

    def __iter__(self):
        return iter(self.__dict__().items())
