import unittest
from tax.categories import BasicDomestic, BasicImported, ExemptDomestic, ExemptImported


class TestTaxCore(unittest.TestCase):

    def test_calculate_sale_tax(self):
        basic_domestic = BasicDomestic()
        # music CD
        self.assertEqual(basic_domestic.calculate_sale_tax(14.99), 1.5)

        basic_imported = BasicImported()
        # imported bottle of perfume
        self.assertEqual(basic_imported.calculate_sale_tax(47.50), 7.15)

        exempt_domestic = ExemptDomestic()
        # book
        self.assertEqual(exempt_domestic.calculate_sale_tax(12.49), 0)

        exempt_imported = ExemptImported()
        # imported box of chocolates
        self.assertEqual(exempt_imported.calculate_sale_tax(10.00), 0.50)


if __name__ == '__main__':
    unittest.main()
