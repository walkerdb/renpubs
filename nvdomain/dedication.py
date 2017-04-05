import re

from nvdomain.constants import LOCATIONS
from util.extraction import extract_location
from util.field_equality_mixin import FieldEqualityMixin


class Dedication(FieldEqualityMixin):
    def __init__(self, dedication):
        self.text = self.extract_text(dedication)
        self.dedicator = self.extract_dedicator(dedication)
        self.dedicatee = self.extract_dedicatee(dedication)
        self.location = extract_location(dedication)

    @staticmethod
    def extract_text(dedication):
        dedication_split = dedication.split(": ", 1)
        if len(dedication_split) is not 2:
            return ""
        return dedication_split[-1].strip('" ')

    @staticmethod
    def extract_dedicator(dedication):
        to_from_text = dedication.split(": ", 1)[0]
        dedicator_regex = re.compile(r"(?<!Conte )(?<!Duca )di ((?:[A-Zd]'?\w+\.? ?)+)|$")
        match = re.findall(dedicator_regex, to_from_text)[0].strip(" .")
        return match if match not in LOCATIONS.keys() and len(match.split(" ")) > 1 else ""

    @staticmethod
    def extract_dedicatee(dedication):
        to_from_text = dedication.split(": ", 1)[0]
        dedicatee_regex = re.compile(r"\b(?:a|ad|al|alli|ai) ((?:Duca di |Conte di |(?:d')?[A-Z][\w']*(?:\. ?| da | del? | d' | )?)+)|$")
        return re.findall(dedicatee_regex, to_from_text)[0].replace("Gentil'huomo", "").strip(" .")
