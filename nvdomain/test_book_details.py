from unittest import TestCase

from nvdomain.book_details import BookDetails


class TestBookDetails(TestCase):
    def test_should_parse_description(self):
        description = BookDetails("4 fasc. in 8° obl., pag. 28(1). ")

        self.assertEquals(description.partbook_count, 4)
        self.assertEquals(description.size, "octavo")
        self.assertEquals(description.is_oblong, True)
        self.assertEquals(description.pages, 28)

    def test_should_have_one_book_if_vol(self):
        description = BookDetails("Vol. in 8° obl., pag. 28(1).")

        self.assertEquals(description.partbook_count, 1)
