from util.field_equality_mixin import FieldEqualityMixin


class Printer(FieldEqualityMixin):
    def __init__(self, name, primary_location=None):
        self.name = name
        self.primary_location = primary_location
