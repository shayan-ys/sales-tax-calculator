from interface.input import file_reader

from cart.receipt import Receipt


def run_by_text_file(data_set_number: int):
    items_data = file_reader('input_set_%d.txt' % data_set_number)

    receipt = Receipt()
    receipt.populate(items_data=items_data)

    print(receipt)


def run_by_json_file(data_set_number: int):
    items_data = file_reader('input_set_%d.txt' % data_set_number)

    receipt = Receipt()
    receipt.populate(items_data=items_data)

    print(receipt)
