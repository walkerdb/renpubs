from unittest import TestCase

from util.extraction import extract_location


class TestExtraction(TestCase):

    def test_converts_antiquated_printer_location(self):
        text = "122 - ARCHADELT Jacques (1575-76) - Title. Appresso di Antonio Gardano in Venetiis"
        location = extract_location(text)

        self.assertEquals(location.modern, "Venice")
        self.assertEquals(location.original, "Venetiis")

    def test_processes_multiple_locations(self):
        text = "122 - ARCHADELT Jacques (1575-76) - Title. Appresso di Antonio Gardano in Roma, no in Venetia"
        location = extract_location(text)

        self.assertEquals(location.modern, "Venice")
