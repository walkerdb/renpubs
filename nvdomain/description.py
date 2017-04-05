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

    @staticmethod
    def extract_description_and_dedication(raw_description):
        _split_desc = re.split(r"Ded\.? ", raw_description)

        dedication = ""
        description = _split_desc[0]
        if len(_split_desc) is 2:
            description, dedication = _split_desc

        return " ".join(description.split("\n")), " ".join(dedication.split("\n"))

    @staticmethod
    def extract_dedication_text(dedication):
        dedication_split = dedication.split(": ", 1)
        if len(dedication_split) is not 2:
            return ""
        return dedication_split[-1].strip('" ')

    @staticmethod
    def extract_dedicator(dedication):
        to_from_text = dedication.split(": ", 1)[0]
        dedicator_regex = re.compile(r"di ((?:[A-Zd]'?\w+\.? ?)+)|$")
        return re.findall(dedicator_regex, to_from_text)[0].strip()

    @staticmethod
    def extract_dedicatee(dedication):
        to_from_text = dedication.split(": ", 1)[0]
        dedicatee_regex = re.compile(r" ad? ((?:[A-Zd]'?\w+\.? ?)+)|$")
        return re.findall(dedicatee_regex, to_from_text)[0].strip()
