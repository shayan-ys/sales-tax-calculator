from .core import Tax


class Basic(Tax):
    basic_tax = 10


class Exempt(Tax):
    basic_tax = 0


class Imported(Tax):
    import_duty = 5


class Domestic(Tax):
    import_duty = 0
