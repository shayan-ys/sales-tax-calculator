# internal
from interface.parser import parse_item, parse_item_from_json

# 1st party
from settings import data_set_dir

# 3rd party
from typing import List, Tuple
import json


def multi_line(raw: str) -> List[Tuple]:
    """
    Example:
        "1 imported box of chocolates at 10.00\n1 imported bottle of perfume at 47.50"
        -> [(1, True, 'box of chocolates', '', 10.0), (1, True, 'bottle of perfume', '', 47.5)]
    :param raw:
    :return: List[(count, imported, name, category_str, price)]
    """
    lines = raw.split('\n')

    return list(map(parse_item, lines))


def file_reader(filename: str) -> List[Tuple]:
    """Read from text file each item written in one line, return pre-defined format of data
    Example:
        file_reader(input_set_2.txt)
        -> [(1, True, 'box of chocolates', '', 10.0), (1, True, 'bottle of perfume', '', 47.5)]
    :param filename: in the project's data folder
    :return: List[(count, imported, name, category_str, price)]
    """
    with open(data_set_dir + filename) as f:
        lines = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    return list(map(parse_item, lines))


def json_file_reader(filename: str) -> List[Tuple]:
    """Read from JSON file, return pre-defined format of data
    Example:
        json_file_reader(input_set_1.txt)
        -> [(1, False, 'book', 'Book', 12.49), (1, False, 'music CD', 'Basic', 14.99),
            (1, False, 'chocolate bar', 'Food', 0.85)]
    :param filename: in the project's data folder
    :return: List[(count, imported, name, category_str, price)]
    """
    with open(data_set_dir + filename) as f:
        data = json.load(f)

    try:
        return list(map(parse_item_from_json, data["items"]))
    except (KeyError, TypeError):
        return []
