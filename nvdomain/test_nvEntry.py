from unittest import TestCase

from nvdomain.description import Description
from nvdomain.header import Header
from nvdomain.librarylocations import LibraryLocations
from nvdomain.nventry import NvEntry
from nvdomain.works import Works


class TestNvEntry(TestCase):
    def test_should_parse_normal_entry(self):
        text = "112 - LAST First (2017) - Work title\n" \
               "\n" \
               "4 fasc. in 8 obl. Ded a Darth Vader di Luke Skywalker.\n" \
               "\n" \
               "A 1. Threnody on Tatooine (Jar Jar Binks)\n" \
               "A 5. Here's something else\n" \
               "\n" \
               "DS-ARg: compl."

        works = Works("A 1. Threnody on Tatooine (Jar Jar Binks)\n"
                      "A 5. Here's something else\n", "", "First Last")

        nv_entry = NvEntry(text)

        self.assertEquals(nv_entry.header, Header("112 - LAST First (2017) - Work title"))
        self.assertEquals(nv_entry.description, Description("4 fasc. in 8 obl. Ded a Darth Vader di Luke Skywalker."))
        self.assertEquals(nv_entry.works.works[0], works.works[0])
        self.assertEquals(nv_entry.works.works[1], works.works[1])
        self.assertEquals(nv_entry.library_locations, LibraryLocations("DS-ARg: compl."))

    def test_should_parse_entry_with_no_works(self):
        text = "112 - LAST First (2017) - Work title\n" \
               "\n" \
               "4 fasc. in 8 obl. Ded a Darth Vader di Luke Skywalker.\n" \
               "\n" \
               "DS-ARg: compl."

        nv_entry = NvEntry(text)

        self.assertEquals(nv_entry.header, Header("112 - LAST First (2017) - Work title"))
        self.assertEquals(nv_entry.description, Description("4 fasc. in 8 obl. Ded a Darth Vader di Luke Skywalker."))
        self.assertEquals(nv_entry.library_locations, LibraryLocations("DS-ARg: compl."))
