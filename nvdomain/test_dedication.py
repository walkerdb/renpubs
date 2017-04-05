from unittest import TestCase

from nvdomain.dedication import Dedication


class TestDedication(TestCase):
    def test_should_parse_dedication(self):
        dedication = Dedication("Ded. di Luke Skywalker a Obi Wan in Anversa: \"hi, 9 I 1630.\"")

        self.assertEquals(dedication.text, "hi, 9 I 1630.")
        self.assertEquals(dedication.dedicator, "Luke Skywalker")
        self.assertEquals(dedication.dedicatee, "Obi Wan")
        self.assertEquals(dedication.location.modern, "Antwerp")
