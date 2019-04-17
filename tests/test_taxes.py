import unittest
from tax.core import Tax


class TestTax(unittest.TestCase):

    def test_round_up_05(self):
        self.assertEqual(Tax.round_up_05(7.124), 7.15)

    def test_calculate_sale_tax(self):
        default_tax = Tax()
        self.assertEqual(default_tax.calculate_sale_tax(47.5), 7.15)


if __name__ == '__main__':
    unittest.main()
