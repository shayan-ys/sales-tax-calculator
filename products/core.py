from tax.core import Tax
import tax.categories


class Product:
    # inputs | modifiable
    tax_profile = Tax       # type: type
    imported = False        # type: bool
    price = 0.0             # type: float
    # automatic values
    tax_processor = None    # type: Tax
    tax_amount = 0.0        # type: float
    cost = 0.0              # type: float

    def __init__(self, price: float, imported: bool = False):
        # change tax profile to imported if necessary
        self.update_imported_tax_profile(imported=imported)
        # ready tax processor to calculate price
        self.tax_processor = self.tax_profile()
        # negative prices are not abstracted, to let app use negative amounts for returned products
        self.price = price
        self.save_tax()
        self.cost = self.price + self.tax_amount

    def save_tax(self):
        """Calculate and save tax_amount using product's tax processor, and based on its price
        :return: void
        """
        self.tax_amount = self.tax_processor.calculate_sale_tax(price=self.price)

    def update_imported_tax_profile(self, imported: bool):
        """Change tax profile if product is imported

        Example:
            BasicDomestic -> BasicImported
        """
        if imported:
            # change Domestic -> Imported tax type based on the product type
            if isinstance(self.tax_profile, tax.categories.BasicDomestic):
                # Basic product
                self.tax_profile = tax.categories.BasicImported
            elif isinstance(self.tax_profile, tax.categories.ExemptDomestic):
                # Exempt product
                self.tax_profile = tax.categories.ExemptImported

        # else tax profile is already from type Imported
