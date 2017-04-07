from unittest import TestCase

from nvdomain.librarylocation import LibraryLocation


class TestLibraryLocation(TestCase):
    def test_parses_basic_library(self):
        location = LibraryLocation("I-Bc: compl.")

        self.assertEquals(location.siglum, "I-Bc")
        self.assertEquals(location.parts, "compl.")

    def test_parses_basic_library_no_parts(self):
        location = LibraryLocation("I-Bc")

        self.assertEquals(location.siglum, "I-Bc")
        self.assertEquals(location.parts, "")

    def test_parses_RISM(self):
        location = LibraryLocation("RISM, I 1567")

        self.assertEquals(location.siglum, "RISM")
        self.assertEquals(location.parts, "1567")

    def test_parses_köln(self):
        location = LibraryLocation("Un esemplare compl. esisteva nella Collezione Heyer di Kòln.")

        self.assertEquals(location.siglum, "Collezione Heyer di Köln")
        self.assertEquals(location.parts, "Un esemplare compl. esisteva nella Collezione Heyer di Kòln.")
