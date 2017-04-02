from unittest import TestCase

from nvdomain import Header


class TestHeader(TestCase):

    def test_processes_header_string(self):
        input = "122 - ARCHADELT Jacques (1575) - Title"
        header = Header(input)

        self.assertEquals("122", header.number)
        self.assertEquals(["Jacques Archadelt"], header.composers)
        self.assertEquals("1575", header.year)
        self.assertEquals("Title", header.title)

    def test_processes_bis(self):
        input = "122 bis - ARCHADELT Jacques (1575) - Title"
        header = Header(input)

        self.assertEquals("122 bis", header.number)

    def test_processes_year_weirdness_questionmark(self):
        input = "122 bis - ARCHADELT Jacques (1575?) - Title"
        header = Header(input)

        self.assertEquals("1575", header.year)

    def test_processes_year_weirdness_dash(self):
        input = "122 bis - ARCHADELT Jacques (1575-76) - Title"
        header = Header(input)

        self.assertEquals("1575", header.year)

    def test_processes_multiple_composers(self):
        input = "122 bis - ARCHADELT Jacques - FESTA Costanza (1575-76) - Title"
        header = Header(input)

        self.assertEquals(["Jacques Archadelt", "Costanza Festa"], header.composers)

    def test_processes_long_composer_names(self):
        input = "122 bis - ARCHADELT JOHN Jacques (1575-76) - Title"
        header = Header(input)

        self.assertEquals(["Jacques Archadelt John"], header.composers)

