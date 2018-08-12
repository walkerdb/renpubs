from nvdomain.description import Description
from nvdomain.header import Header
from nvdomain.librarylocations import LibraryLocations
from nvdomain.works import Works
from util.field_equality_mixin import FieldEqualityMixin


class NvEntry(FieldEqualityMixin):
    def __init__(self, text):
        header_text, description_text, works, locations = self.extract_sections(text)

        self.header = Header(header_text)
        self.description = Description(description_text)
        self.works = Works(works, self.header.get_default_voices(), self.header.get_default_composer())
        self.library_locations = LibraryLocations(locations)

    @staticmethod
    def extract_sections(text):
        data = text.strip("\n").split("\n\n")
        title = meta = works = locations = ""

        if len(data) is 3:
            title, meta, locations = data

        elif len(data) is 4:
            title, meta, works, locations = data

        else:
            pass

        if len(locations.split("\n")) > 13:
            works = locations
            locations = ""

        title = title.replace("\n", " ")

        return title, meta, works, locations
