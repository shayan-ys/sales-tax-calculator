import unittest
import sys
from tax.core import Tax


class TestTaxCore(unittest.TestCase):

    def test_round_up_05(self):
        self.assertEqual(Tax.round_up_05(7.124), 7.15)
        # extreme conditions
        self.assertEqual(0, Tax.round_up_05(0))
        self.assertEqual(0, Tax.round_up_05(0.000000))
        self.assertEqual(0, Tax.round_up_05(0.000000000000000000000000000000000000000000000000000000000000000000000001))
        self.assertEqual(0.05, Tax.round_up_05(0.05))
        self.assertEqual(0.05, Tax.round_up_05(0.0001))
        self.assertEqual(0.05, Tax.round_up_05(0.049999999999999999999999999999999999999999999999999999999999999999999))
        self.assertEqual(0.1, Tax.round_up_05(0.1))
        self.assertEqual(0.1, Tax.round_up_05(0.10))
        self.assertEqual(0.1, Tax.round_up_05(0.0999999999999999999999999999999999999999999999999999999999999999999999))
        self.assertEqual(922337203685477.05, Tax.round_up_05(922337203685477.0001))
        self.assertEqual(0, Tax.round_up_05(-0))
        self.assertEqual(-0.1, Tax.round_up_05(-0.05001))
        self.assertEqual(-0.05, Tax.round_up_05(-0.050001))
        self.assertEqual(-0.05, Tax.round_up_05(-0.01))
        self.assertEqual(-0.05, Tax.round_up_05(-0.0499999999999999999999999999999999999999999999999999999999999999999))
        self.assertEqual(-0.05, Tax.round_up_05(-0.05))
        self.assertEqual(-922337203685477.05, Tax.round_up_05(-922337203685477.0001))

    def test_calculate_sale_tax(self):
        default_tax = Tax()
        default_tax.basic_tax = 10
        default_tax.import_duty = 5
        self.assertEqual(7.15, default_tax.calculate_sale_tax(47.5))


if __name__ == '__main__':
    unittest.main()
