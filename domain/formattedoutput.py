from domain.model import Publication
from util.field_equality_mixin import FieldEqualityMixin


class FormattedOutput(FieldEqualityMixin):
    def __init__(self, entries):
        self.publications = [Publication(entry) for entry in entries]