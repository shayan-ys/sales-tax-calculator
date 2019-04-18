from product.core import Product


class Item:
    """Container to store multiple count of same product in the receipt
    Usage:
        cart.receipt.Receipt
    """
    product = None      # type: Product
    count = 0           # type: int

    def __init__(self, product_obj: Product, count: int):
        self.product = product_obj
        self.count = count
