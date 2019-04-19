# in-module
from .types import BasicProduct, ExemptProduct

# 3rd party
from typing import Type, Union


class Book(ExemptProduct):
    pass


class Food(ExemptProduct):
    pass


class Medical(ExemptProduct):
    pass


class Basic(BasicProduct):
    pass


keywords = {
    "book": Book,
    "books": Book,
    "chocolate": Food,
    "chocolates": Food,
    "fruit": Food,
    "fruits": Food,
    "pasta": Food,
    "pastas": Food,
    "pill": Medical,
    "pills": Medical,
    "headache": Medical
}
category_names = {
    "Book": Book,
    "Food": Food,
    "Medical": Medical
}


def category_identifier(product_title: str) -> Type[Union[Book, Food, Medical, Basic]]:
    """Identify product category using its name and a dictionary of keywords
    :param product_title:
    :return:
    """
    for word in product_title.split():
        try:
            return keywords[word]
        except KeyError:
            # given word doesn't exist in keywords dictionary
            pass

    return Basic


def category_class_by_name(category_str: str) -> Type[Union[Book, Food, Medical, Basic]]:
    """Return product's category by its name
    :param category_str:
    :return: product's category class
    """
    try:
        return category_names[category_str]
    except KeyError:
        return Basic
