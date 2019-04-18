import constant
# 1 imported bottle of perfume at 47.50


raw = "1 imported bottle of perfume at 47.50"

raw_n_price = raw.split("at")
print(raw_n_price)

if len(raw_n_price) > 1:
    # price found
    price_str = raw_n_price[1].strip()

    try:
        price = float(price_str)
    except ValueError:
        price = 0.0

    print(type(price))
    print(price)

    count_n_raw = raw_n_price[0].split(maxsplit=1)

    print(count_n_raw)

    if len(count_n_raw) > 1:
        count_str = count_n_raw[0].strip()

        try:
            count = int(count_str)
        except ValueError:
            count = 1

        print(type(count))
        print(count)

        if count_n_raw[1].strip().startswith(constant.Strings.IMPORTED):
            imported = True
        else:
            imported = False

        imported_n_name = count_n_raw[1].split(constant.Strings.IMPORTED)
        name = imported_n_name[-1].strip()

        print("imported" if imported else "domestic")
        print(name)
