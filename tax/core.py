from decimal import ROUND_UP
from decimal import Decimal


class Tax:
    """General Tax

    Encapsulates common methods and attributes to use for all kinds of taxes
    Specific kinds of taxes will be derived from this
    Every product will have a tax instance as well

    Attributes:
        :var basic_tax (int): basic sales tax, applicable at a rate of 10% on all goods,
            except books, food, and medical products, which are exempt.
            written in format of n%, therefore saving as integers. e.g., 10% tax -> basic_tax = 10.
            Default to 10.
        :var import_duty (int): Import duty is an additional sales tax applicable on all imported goods at a rate of 5%,
            with no exemptions.
            written in format of n%, therefore saving as integers. e.g., 5% tax -> import_duty = 5.
            Default to 5.
    """

    # tax percentages (basic tax: 5%, import duty: 10%)
    basic_tax = 10      # type: int
    import_duty = 5     # type: int

    @staticmethod
    def round_up_05(amount: float) -> float:
        """Round up amount to nearest 0.05
        Rounding x to nearest 0.05 is the same as rounding x*2 to nearest 0.1, returning half the result

        Example:
            7.124 * 2 = 14.248
            round up to the nearest 0.1 -> 14.3
            14.3 / 2 = 7.15

        :param float amount: raw, not rounded number
        :return: amount rounded up to the nearest 0.05
        """
        return float(Decimal(amount * 2).quantize(Decimal('.1'), rounding=ROUND_UP) / 2)

    def calculate_sale_tax(self, price: float) -> float:
        """Calculate final tax for a given product price
        Add all taxes * product price -> round up to nearest 0.05

        Example:
            price = 47.5, basic_tax = 10, import_duty = 5 => sale tax = 7.15

        :param price:
        :return:
        """
        aggregated_tax = self.basic_tax + self.import_duty
        raw_tax = aggregated_tax * price / 100
        return Tax.round_up_05(raw_tax)
        # return Tax.round_up_05((self.basic_tax + self.import_duty) * price / 100)
