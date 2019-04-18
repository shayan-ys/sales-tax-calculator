# internal
from interface.parser import parse_item

# 1st party
from settings import data_set_dir

# 3rd party
from typing import List, Tuple


def multi_line(raw: str) -> List[Tuple]:
    """
    Example:
        "1 imported box of chocolates at 10.00\n1 imported bottle of perfume at 47.50"
        -> [(1, True, 'box of chocolates', 10.0), (1, True, 'bottle of perfume', 47.5)]
    :param raw:
    :return: count, imported, name, price
    """
    lines = raw.split('\n')

    return list(map(parse_item, lines))


def file_reader(filename: str) -> List[Tuple]:
    with open(filename) as f:
        lines = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    return list(map(parse_item, lines))
