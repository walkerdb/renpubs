import re

from util.field_equality_mixin import FieldEqualityMixin


class LibraryLocation(FieldEqualityMixin):
    def __init__(self, text):
        self.siglum = self.extract_siglum(text)
        self.parts = self.extract_parts(text)

    @staticmethod
    def extract_siglum(text):
        if "Collezione Heyer" in text:
            return "Collezione Heyer di Köln"
        if "RISM" in text:
            return "RISM"
        if "Sartori" in text:
            return "Sartori"
        return text.split(": ")[0].strip(" -")

    @staticmethod
    def extract_parts(text):
        if "Collezione Heyer" in text:
            return text
        if "RISM" in text:
            return re.split(r" I,? ", text)[-1]
        if "Sartori" in text:
            return text.replace("Sartori", "").strip()
        if ": " not in text:
            return ""
        return text.split(": ", 1)[-1].strip(" -")