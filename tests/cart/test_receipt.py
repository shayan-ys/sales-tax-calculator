import unittest

from product.categories import Book, Food, Medical, Basic
from cart.receipt import Receipt

from interface.input import file_reader


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


class TestReceiptPrint(unittest.TestCase):

    def test_receipt_str(self):
        book = Book(12.49)
        music_cd = Basic(14.99, name='music CD')
        chocolate = Food(0.85, name='chocolate bar')

        receipt_1 = Receipt()
        receipt_1.add(book)
        receipt_1.add(music_cd)
        receipt_1.add(chocolate)

        expected = "1 book: 12.49\n1 music CD: 16.49\n1 chocolate bar: 0.85\nSales Taxes: 1.50\nTotal: 29.83"
        self.assertEqual(expected, str(receipt_1))

        receipt_empty = Receipt()
        expected = "\nSales Taxes: 0.00\nTotal: 0.00"
        self.assertEqual(expected, str(receipt_empty))

    def test_receipt_dict(self):
        book = Book(12.49)
        music_cd = Basic(14.99, name='music CD')
        chocolate = Food(0.85, name='chocolate bar')

        receipt_1 = Receipt()
        receipt_1.add(book)
        receipt_1.add(music_cd)
        receipt_1.add(chocolate)

        expected = {
            'items': [
                {'cost': 12.49,
                 'count': 1,
                 'imported': False,
                 'product': 'book',
                 'tax': 0.0},
                {'cost': 16.49,
                 'count': 1,
                 'imported': False,
                 'product': 'music CD',
                 'tax': 1.5},
                {'cost': 0.85,
                 'count': 1,
                 'imported': False,
                 'product': 'chocolate bar',
                 'tax': 0.0}
            ],
            'total cost': 29.83,
            'total sale taxes': 1.5
        }
        self.assertEqual(expected, receipt_1.__dict__())

        receipt_empty = Receipt()
        expected = {
            'items': [],
            'total cost': 0,
            'total sale taxes': 0
        }
        self.assertEqual(expected, receipt_empty.__dict__())


class TestCart(unittest.TestCase):
    def test_populate(self):
        items_data = file_reader('input_set_1.txt')
        receipt = Receipt()
        receipt.populate(items_data)

        expected = "1 book: 12.49\n1 music CD: 16.49\n1 chocolate bar: 0.85\nSales Taxes: 1.50\nTotal: 29.83"
        self.assertEqual(expected, str(receipt))

        items_data = file_reader('input_set_2.txt')
        receipt = Receipt()
        receipt.populate(items_data)

        expected = "1 imported box of chocolates: 10.50\n1 imported bottle of perfume: 54.65\nSales Taxes: 7.65" \
                   "\nTotal: 65.15"
        self.assertEqual(expected, str(receipt))

        items_data = file_reader('input_set_3.txt')
        receipt = Receipt()
        receipt.populate(items_data)

        expected = "1 imported bottle of perfume: 32.19\n1 bottle of perfume: 20.89" \
                   "\n1 packet of headache pills: 9.75" \
                   "\n1 imported box of chocolates: 11.85\nSales Taxes: 6.70\nTotal: 74.68"
        self.assertEqual(expected, str(receipt))


if __name__ == '__main__':
    unittest.main()
