import unittest

from product.categories import Book, Food, Medical, Basic
from cart.receipt import Receipt


class TestReceipt(unittest.TestCase):
    def test_total_tax(self):
        book = Book(12.49)
        music_cd = Basic(14.99)
        chocolate = Food(0.85)

        receipt_1 = Receipt()
        receipt_1.add(book)
        receipt_1.add(music_cd)
        receipt_1.add(chocolate)

        self.assertEqual(1.50, receipt_1.total_tax_amount)

        imported_chocolate = Food(10, imported=True)
        imported_perfume = Basic(47.50, imported=True)

        receipt_2 = Receipt()
        receipt_2.add(imported_chocolate)
        receipt_2.add(imported_perfume)

        self.assertEqual(7.65, receipt_2.total_tax_amount)

        imported_perfume_2 = Basic(27.99, imported=True)
        perfume = Basic(18.99)
        headache_pills = Medical(9.75)
        imported_chocolate_2 = Food(11.25, imported=True)

        receipt_3 = Receipt()
        receipt_3.add(imported_perfume_2)
        receipt_3.add(perfume)
        receipt_3.add(headache_pills)
        receipt_3.add(imported_chocolate_2)

        self.assertEqual(6.70, receipt_3.total_tax_amount)

    def test_total_cost(self):
        book = Book(12.49)
        music_cd = Basic(14.99)
        chocolate = Food(0.85)

        receipt_1 = Receipt()
        receipt_1.add(book)
        receipt_1.add(music_cd)
        receipt_1.add(chocolate)

        self.assertEqual(29.83, receipt_1.total_cost)

        imported_chocolate = Food(10, imported=True)
        imported_perfume = Basic(47.50, imported=True)

        receipt_2 = Receipt()
        receipt_2.add(imported_chocolate)
        receipt_2.add(imported_perfume)

        self.assertEqual(65.15, receipt_2.total_cost)

        imported_perfume_2 = Basic(27.99, imported=True)
        perfume = Basic(18.99)
        headache_pills = Medical(9.75)
        imported_chocolate_2 = Food(11.25, imported=True)

        receipt_3 = Receipt()
        receipt_3.add(imported_perfume_2)
        receipt_3.add(perfume)
        receipt_3.add(headache_pills)
        receipt_3.add(imported_chocolate_2)

        self.assertEqual(74.68, receipt_3.total_cost)

    def test_multi_count_receipt(self):
        imported_chocolate = Food(10, imported=True)
        imported_perfume = Basic(47.50, imported=True)

        receipt_2 = Receipt()
        receipt_2.add(imported_chocolate, count=2)
        receipt_2.add(imported_perfume, count=3)
        receipt_2.add(imported_chocolate, count=3)

        self.assertEqual(23.95, receipt_2.total_tax_amount)
        self.assertEqual(216.45, receipt_2.total_cost)


if __name__ == '__main__':
    unittest.main()
