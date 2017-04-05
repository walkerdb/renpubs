import re

from util.field_equality_mixin import FieldEqualityMixin

size_map = {
    "4": "quarto",
    "8": "octavo"
}


class BookDescription(FieldEqualityMixin):
    def __init__(self, description):
        self.count = self.extract_book_count(description)
        self.size = self.extract_book_size(description)
        self.pages = self.extract_pages(description)
        self.is_oblong = " obl." in description

    @staticmethod
    def extract_book_count(description):
        count = re.findall(r"(\d+) fasc\.|$", description)[0]
        if not count:
            if re.findall(r"^Vol\.? ", description):
                return 1
            return ""

        return int(count)

    @staticmethod
    def extract_book_size(description):
        return size_map.get(re.findall(r"in ([48])° |$", description)[0], "")

    @staticmethod
    def extract_pages(description):
        page_numbers = re.findall(r"pag\.? (\d+)|$", description)[0]
        if not page_numbers:
            return ""
        return int(page_numbers)
