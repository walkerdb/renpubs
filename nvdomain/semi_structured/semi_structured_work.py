from pprint import pprint

from nvdomain.description import Description
from nvdomain.header import Header
from nvdomain.librarylocations import LibraryLocations
from nvdomain.semi_structured.works import Works
from util.field_equality_mixin import FieldEqualityMixin


class SemiStructuredWorkParser(FieldEqualityMixin):
    def __init__(self, text, entries_so_far=[]):
        header_text, description_text, works, locations = self.extract_sections(text)

        self.raw_text = text
        try:
            self.header = Header(header_text)

            self.description = Description(description_text)
            self.library_locations = LibraryLocations(locations)
            self.works = Works(works, self.header.get_default_voices(), self.header.get_default_composer())

            works_are_described_in_other_book = bool(self.description.index)
            if works_are_described_in_other_book:
                self.assign_works_from_past_entry(entries_so_far)
        except Exception as e:
            print("Header: " + header_text)
            print("Description: " + description_text)
            pprint("Works: " + works)
            print("Locations: " + locations)
            print(text)
            raise e

    def assign_works_from_past_entry(self, entries_so_far):
        for entry in reversed(entries_so_far):
            has_gone_too_far = entry.header.get_default_composer() != self.header.get_default_composer()
            if has_gone_too_far:
                break

            has_found_valid_index_reference = entry.header.year_index.strip("()") == self.description.index and len(entry.works.works) > 1
            if has_found_valid_index_reference:
                self.works = entry.works
                break

        if len(self.works.works) <= 1:
            print("wtf I have no works {}".format(self.header.number))
            self.works.works = []

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

        title = title.replace("\n", " ")

        return title, meta, works, locations
