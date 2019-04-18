import unittest

from cart.item import Item
from product.categories import Book, Basic


class TestItem(unittest.TestCase):
    def test_dict(self):
        book = Book(12, imported=True, name='Little Princess book')
        item = Item(book, 3)
        expected = {'count': 3, 'imported': True, 'product': 'imported Little Princess book', 'tax': 1.8, 'cost': 37.8}
        self.assertEqual(expected, item.__dict__())

        perfume = Basic(23)
        item_perfume = Item(perfume, 2)
        expected = {'count': 2, 'imported': False, 'product': 'basic', 'tax': 4.6, 'cost': 50.6}
        self.assertEqual(expected, item_perfume.__dict__())

    def test_str(self):
        book = Book(12, imported=True, name='Little Princess book')
        item = Item(book, 3)
        self.assertEqual("3 imported Little Princess book: 37.80", str(item))


if __name__ == '__main__':
    unittest.main()
