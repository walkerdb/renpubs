from unittest import TestCase

from nvdomain.description import Description
from nvdomain.header import Header
from nvdomain.librarylocations import LibraryLocations
from nvdomain.semi_structured.semi_structured_work import SemiStructuredWorkParser
from nvdomain.semi_structured.works import Works


class TestSemiStructuredWorkParser(TestCase):
    def test_should_parse_normal_entry(self):
        text = """
112 - LAST First (2017) - Work title Girolamo Scotto

4 fasc. in 8 obl. Ded a Darth Vader di Luke Skywalker.

A 4	1. Work with 4 voices, first part and new composer  	-            	New Composer	-                 	 2
-	2. Work with 4 voices, second part                             	Seconda parte	New Composer	-                 	 3

DS-ARg: compl.
"""

        works = Works("A 4	1. Work with 4 voices, first part and new composer  	-            	New Composer	-                 	 2\n"
                      "-	2. Work with 4 voices, second part                             	Seconda parte	New Composer	-                 	 3\n",
                      "4", "Default Composer")

        nv_entry = SemiStructuredWorkParser(text)

        self.assertEquals(nv_entry.header, Header("112 - LAST First (2017) - Work title Girolamo Scotto"))
        self.assertEquals(nv_entry.description, Description("4 fasc. in 8 obl. Ded a Darth Vader di Luke Skywalker."))
        self.assertEquals(nv_entry.works.works[0], works.works[0])
        self.assertEquals(nv_entry.works.works[1], works.works[1])
        self.assertEquals(nv_entry.library_locations, LibraryLocations("DS-ARg: compl."))

    def test_should_parse_entry_with_no_works(self):
        text = "112 - LAST First (2017) - Work title Girolamo Scotto\n" \
               "\n" \
               "4 fasc. in 8 obl. Ded a Darth Vader di Luke Skywalker.\n" \
               "\n" \
               "DS-ARg: compl."

        nv_entry = SemiStructuredWorkParser(text)

        self.assertEquals(nv_entry.header, Header("112 - LAST First (2017) - Work title Girolamo Scotto"))
        self.assertEquals(nv_entry.description, Description("4 fasc. in 8 obl. Ded a Darth Vader di Luke Skywalker."))
        self.assertEquals(nv_entry.library_locations, LibraryLocations("DS-ARg: compl."))
