import re

from nvdomain.book_details import BookDetails
from nvdomain.dedication import Dedication
from util.field_equality_mixin import FieldEqualityMixin


class Description(FieldEqualityMixin):
    def __init__(self, raw_description):
        description, dedication = self.extract_description_and_dedication(raw_description)
        self.raw_description = description
        self.raw_dedication = dedication
        self.book_details = BookDetails(description)
        self.dedication = Dedication(dedication)
        self.index = self.extract_index(raw_description)

    @staticmethod
    def extract_description_and_dedication(raw_description):
        _split_desc = re.split(r"Ded\.? ", raw_description)

        dedication = ""
        description = _split_desc[0]
        if len(_split_desc) is 2:
            description, dedication = _split_desc
            dedication = dedication.split("Indice")[0]

        return " ".join(description.split("\n")), " ".join(dedication.split("\n"))

    @staticmethod
    def extract_index(text):
        return re.findall(r"Indice ?[=:] ?((?:[\d\-]+|al preced))|$", text)[0].strip("- ")