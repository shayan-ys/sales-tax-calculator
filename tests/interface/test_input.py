import unittest
from interface.input import multi_line, file_reader

from settings import data_set_dir


class TestInputText(unittest.TestCase):
    def test_multi_line(self):
        self.assertEqual([(1, True, 'box of chocolates', 10.0), (1, True, 'bottle of perfume', 47.5)], multi_line("1 imported box of chocolates at 10.00\n1 imported bottle of perfume at 47.50"))


class TestInputFile(unittest.TestCase):
    def test_input_set(self):
        self.assertEqual([(1, False, 'book', 12.49), (1, False, 'music CD', 14.99), (1, False, 'chocolate bar', 0.85)],
                         file_reader(data_set_dir + 'input_set_1.txt'))

        self.assertEqual([(1, True, 'box of chocolates', 10.0), (1, True, 'bottle of perfume', 47.5)],
                         file_reader(data_set_dir + 'input_set_2.txt'))


if __name__ == '__main__':
    unittest.main()
