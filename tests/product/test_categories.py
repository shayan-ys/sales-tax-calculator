import unittest
from product.categories import Book, Food, Medical, Basic

import tax.categories


class TestProductCategories(unittest.TestCase):
    def test_tax_profile(self):
        book = Book(12.49)
        self.assertEqual(tax.categories.ExemptDomestic, book.tax_profile)
        music_cd = Basic(14.99)
        self.assertEqual(tax.categories.BasicDomestic, music_cd.tax_profile)
        chocolate = Food(0.85)
        self.assertEqual(tax.categories.ExemptDomestic, chocolate.tax_profile)
        imported_chocolate = Food(10, imported=True)
        self.assertEqual(tax.categories.ExemptImported, imported_chocolate.tax_profile)
        imported_perfume = Basic(47.50, imported=True)
        self.assertEqual(tax.categories.BasicImported, imported_perfume.tax_profile)
        perfume = Basic(18.99)
        self.assertEqual(tax.categories.BasicDomestic, perfume.tax_profile)
        headache_pills = Medical(9.75)
        self.assertEqual(tax.categories.ExemptDomestic, headache_pills.tax_profile)

    def test_cost(self):
        book = Book(12.49)
        self.assertEqual(12.49, book.cost)
        music_cd = Basic(14.99)
        self.assertEqual(16.49, music_cd.cost)
        chocolate = Food(0.85)
        self.assertEqual(0.85, chocolate.cost)
        imported_chocolate = Food(10, imported=True)
        self.assertEqual(10.50, imported_chocolate.cost)
        imported_perfume = Basic(47.50, imported=True)
        self.assertEqual(54.65, imported_perfume.cost)
        perfume = Basic(18.99)
        self.assertEqual(20.89, perfume.cost)
        headache_pills = Medical(9.75)
        self.assertEqual(9.75, headache_pills.cost)

        # extreme conditions
        self.assertEqual(11.50, Basic(10.0, imported=True).cost)
        self.assertEqual(11.50, Basic(10.00001, imported=True).cost)
        self.assertEqual(11.55, Basic(10.001, imported=True).cost)


if __name__ == '__main__':
    unittest.main()
