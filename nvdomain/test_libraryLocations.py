from unittest import TestCase

from nvdomain.librarylocations import LibraryLocations


class TestLibraryLocations(TestCase):
    def test_parses_basic_library(self):
        locations = LibraryLocations(
            "I-Bc: compl.\n"
            "D-Db: C.A.T.B.\n"
            "US-UC: cats"
        )

        self.assertEquals(locations.libraries[0].siglum, "I-Bc")
        self.assertEquals(locations.libraries[0].parts, "compl.")

        self.assertEquals(locations.libraries[1].siglum, "D-Db")
        self.assertEquals(locations.libraries[1].parts, "C.A.T.B.")

        self.assertEquals(locations.libraries[2].siglum, "US-UC")
        self.assertEquals(locations.libraries[2].parts, "cats")
