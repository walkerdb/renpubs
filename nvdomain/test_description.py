from unittest import TestCase

from nvdomain.book_details import BookDetails
from nvdomain.dedication import Dedication
from nvdomain.description import Description


class TestDescription(TestCase):

    def test_should_parse_description(self):
        description = Description("4 fasc. in 8° obl., pag. 28(1). Ded. di Luke Skywalker a Obi Wan in Anversa: \"hi, 9 I 1630.\" Indice = 1571-4.")

        self.assertEquals(description.book_details, BookDetails("4 fasc. in 8° obl., pag. 28(1)"))
        self.assertEquals(description.dedication, Dedication(" Ded. di Luke Skywalker a Obi Wan in Anversa: \"hi, 9 I 1630.\""))
        self.assertEquals(description.index, "1571-4")
