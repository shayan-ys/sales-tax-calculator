import unittest
from interface.parser import parse_item


class TestParser(unittest.TestCase):
    def test_parse_item_str(self):
        self.assertEqual((1, True, "bottle of perfume", 47.5),
                         parse_item("1 imported bottle of perfume at 47.50"))
        self.assertEqual((1, True, "box of chocolates", 10),
                         parse_item("1 imported box of chocolates at 10.00"))
        self.assertEqual((1, False, "night at museum book", 25.5),
                         parse_item("1 night at museum book at 25.5"))

        # extreme conditions
        # TODO: self.assertEqual((), parse_item(""))
        self.assertEqual((1, False, 'pill', 0.0), parse_item("pill"))
        self.assertEqual((1, False, 'headache pill', 0.0), parse_item("headache pill"))
        # TODO: self.assertEqual((1, False, 'at', 0.0), parse_item("at"))


if __name__ == '__main__':
    unittest.main()
