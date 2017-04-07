from nvdomain.librarylocation import LibraryLocation
from util.field_equality_mixin import FieldEqualityMixin


class LibraryLocations(FieldEqualityMixin):
    def __init__(self, text):
        self.libraries = self.extract_library_locations(text)

    def extract_library_locations(self, text):
        return [LibraryLocation(line) for line in text.strip(" \n").split("\n")]