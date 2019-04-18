from .types import Basic, Exempt, Domestic, Imported


class BasicDomestic(Basic, Domestic):
    pass


class BasicImported(Basic, Imported):
    pass


class ExemptDomestic(Exempt, Domestic):
    pass


class ExemptImported(Exempt, Imported):
    pass
