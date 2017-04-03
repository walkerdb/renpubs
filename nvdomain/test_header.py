from unittest import TestCase

from nvdomain import Header


class TestHeader(TestCase):

    def test_processes_header_string(self):
        input = "122 - ARCHADELT Jacques (1575) - " \
                "Il Primo libro de Madrigali a 4. In Venice, appresso Antonio Gardano, 1592"
        header = Header(input)

        self.assertEquals(header.number, "122")
        self.assertEquals(header.composers, ["Jacques Archadelt"])
        self.assertEquals(header.year, "1575")
        self.assertEquals(header.title, "Il Primo libro de Madrigali a 4. In Venice, appresso Antonio Gardano, 1592")
        self.assertEquals(header.printing_location.modern, "Venice")
        self.assertEquals(header.printers[0].modern, "Antonio Gardano")

    def test_processes_bis(self):
        input = "122 bis - ARCHADELT Jacques (1575) - Title"
        header = Header(input)

        self.assertEquals(header.number, "122 bis")

    def test_processes_year_weirdness_questionmark(self):
        input = "122 - ARCHADELT Jacques (1575?) - Title"
        header = Header(input)

        self.assertEquals(header.year, "1575")

    def test_processes_year_weirdness_dash(self):
        input = "122 - ARCHADELT Jacques (1575-76) - Title"
        header = Header(input)

        self.assertEquals(header.year, "1575")

    def test_processes_multiple_composers(self):
        input = "122 - ARCHADELT Jacques - FESTA Costanza (1575-76) - Title"
        header = Header(input)

        self.assertEquals(header.composers, ["Jacques Archadelt", "Costanza Festa"])

    def test_processes_long_composer_names(self):
        input = "122 - ARCHADELT JOHN Jacques (1575-76) - Title"
        header = Header(input)

        self.assertEquals(header.composers, ["Jacques Archadelt John"])

    def test_converts_antiquated_printer_location(self):
        input = "122 - ARCHADELT Jacques (1575-76) - Title. Appresso di Antonio Gardano in Venetiis"
        header = Header(input)

        self.assertEquals(header.printing_location.modern, "Venice")
        self.assertEquals(header.printing_location.original, "Venetiis")

    def test_processes_multiple_locations(self):
        input = "122 - ARCHADELT Jacques (1575-76) - Title. Appresso di Antonio Gardano in Roma, no in Venetia"
        header = Header(input)

        self.assertEquals(header.printing_location.modern, "Venice")

    def test_converts_antiquated_printer_names(self):
        input = "122 - ARCHADELT Jacques (1575-76) - Title. Appresso di Antonium Gardane in Venetiis"
        header = Header(input)

        self.assertEquals(header.printers[0].modern, "Antonio Gardano")
        self.assertEquals(header.printers[0].original, "Antonium Gardane")

    def test_processes_multiple_printers(self):
        input = "122 - ARCHADELT Jacques (1575-76) - Title. Appresso di Antonio Gardane e Girolamo Scotto in Venetiis"
        header = Header(input)

        self.assertEquals(len(header.printers), 2)
        self.assertEquals(header.printers[0].modern, "Antonio Gardano")
        self.assertEquals(header.printers[1].modern, "Girolamo Scotto")
