import constant
# 1 imported bottle of perfume at 47.50


def parse_item(raw: str) -> (int, bool, str, float):
    """Parse shopping list input strings to get count, imported or not, name of item and item's price
    Example:
        (1, True, "bottle of perfume", 47.50) = parse_item("1 imported bottle of perfume at 47.50")
    :param raw:
    :return: count, imported, name, price
    """
    # defaults in case attributes are not found
    count = 1
    imported = False
    # name = ''
    price = 0.0

    # split the last occurrence of word "at" and look only for one of them
    # note: item's title might have word "at" in it, like "1 night at museum book at 25.5"
    raw_n_price = raw.strip().rsplit("at", maxsplit=1)

    if len(raw_n_price) > 1:
        # price found
        price_str = raw_n_price[1].strip()

        try:
            price = float(price_str)
        except ValueError:
            # price = 0.0 because after the word "at" no number found
            pass

    # split by first space to get the first number in the input which should be the item's count
    count_n_raw = raw_n_price[0].split(maxsplit=1)

    if len(count_n_raw) > 1:
        count_str = count_n_raw[0].strip()

        try:
            count = int(count_str)
        except ValueError:
            # count = 1 because input string hasn't started with a number (for count)
            # reverse split, because the first word wasn't a number so it's part of the title
            count_n_raw[1] = raw_n_price[0]

    # the other half of count (if there was a count), note this array has length of 1 or 2
    # reason: split returns array of at least length 1. max split is set to 1, so array's max length is 2
    raw_import_title = count_n_raw[-1].strip()

    if raw_import_title.startswith(constant.Strings.IMPORTED):
        imported = True

        # split first occurrence of word "imported"
        # note: item title may have word "imported" in it,
        # like "1 how imported cars changed the car industry in US at 15.24"
        imported_n_name = raw_import_title.split(constant.Strings.IMPORTED, maxsplit=1)
        # the other half of imported, which is item's title
        name = imported_n_name[-1].strip()
    else:
        # input hasn't started with word "imported", so don't split any thing the whole string is the title
        # note: the item's title might actually start with the word "imported" and that'd just be a bug in the logic
        #   with this method of input, it is inevitable
        name = raw_import_title

    return count, imported, name, price
