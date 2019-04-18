import unittest
from tax.categories import BasicDomestic, BasicImported, ExemptDomestic, ExemptImported


class TestTaxCategories(unittest.TestCase):

    def test_calculate_sale_tax(self):
        basic_domestic = BasicDomestic()
        # music CD
        self.assertEqual(1.5, basic_domestic.calculate_sale_tax(14.99))

        basic_imported = BasicImported()
        # imported bottle of perfume
        self.assertEqual(7.15, basic_imported.calculate_sale_tax(47.50))

        exempt_domestic = ExemptDomestic()
        # book
        self.assertEqual(0, exempt_domestic.calculate_sale_tax(12.49))

        exempt_imported = ExemptImported()
        # imported box of chocolates
        self.assertEqual(0.50, exempt_imported.calculate_sale_tax(10.00))

        # extreme conditions
        self.assertEqual(0, basic_domestic.calculate_sale_tax(0))
        self.assertEqual(0.05, basic_domestic.calculate_sale_tax(0.05))
        self.assertEqual(0.05, basic_domestic.calculate_sale_tax(0.0001))
        self.assertEqual(100000000000, basic_domestic.calculate_sale_tax(999999999999.99999))
        self.assertEqual(-0.05, basic_domestic.calculate_sale_tax(-0.0001))
        self.assertEqual(0, basic_domestic.calculate_sale_tax(-0))

        self.assertEqual(0, basic_imported.calculate_sale_tax(0))
        self.assertEqual(0.05, basic_imported.calculate_sale_tax(0.05))
        self.assertEqual(0.05, basic_imported.calculate_sale_tax(0.0001))
        self.assertEqual(150000000000, basic_imported.calculate_sale_tax(999999999999.99999))
        self.assertEqual(-0.05, basic_imported.calculate_sale_tax(-0.0001))
        self.assertEqual(0, basic_imported.calculate_sale_tax(-0))

        self.assertEqual(0, exempt_domestic.calculate_sale_tax(0))
        self.assertEqual(0, exempt_domestic.calculate_sale_tax(0.05))
        self.assertEqual(0, exempt_domestic.calculate_sale_tax(0.0001))
        self.assertEqual(0, exempt_domestic.calculate_sale_tax(999999999999.99999))
        self.assertEqual(0, exempt_domestic.calculate_sale_tax(-0.0001))
        self.assertEqual(0, exempt_domestic.calculate_sale_tax(-0))

        self.assertEqual(0, exempt_imported.calculate_sale_tax(0))
        self.assertEqual(0.05, exempt_imported.calculate_sale_tax(0.05))
        self.assertEqual(0.05, exempt_imported.calculate_sale_tax(0.0001))
        self.assertEqual(50000000000, exempt_imported.calculate_sale_tax(999999999999.99999))
        self.assertEqual(-0.05, exempt_imported.calculate_sale_tax(-0.0001))
        self.assertEqual(0, exempt_imported.calculate_sale_tax(-0))


if __name__ == '__main__':
    unittest.main()
