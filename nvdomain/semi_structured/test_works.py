from unittest import TestCase

from nvdomain.semi_structured.works import Works


class TestWorks(TestCase):
    def test_basic_works_processing(self):
        works = Works(
            """
-	Work 1                 	-            	-	-                 	 1
A 4	1. Work with 4 voices, first part and new composer  	-            	New Composer	-                 	 2
-	2. Work with 4 voices, second part                             	Seconda parte	New Composer	-                 	 3
-	Work with 4 voices, with poet                                 	-            	-	Francesco Petrarca	 4""",
            5, "Default Composer")

        self.assertEquals(works.works[0].voices, 5)
        self.assertEquals(works.works[1].voices, 4)
        self.assertEquals(works.works[2].voices, 4)
        self.assertEquals(works.works[3].voices, 4)

        self.assertEquals(works.works[0].title, "Work 1")
        self.assertEquals(works.works[1].title, "Work with 4 voices, first part and new composer")
        self.assertEquals(works.works[2].title, "Work with 4 voices, second part")
        self.assertEquals(works.works[3].title, "Work with 4 voices, with poet")

        self.assertEquals(works.works[0].poet, "")
        self.assertEquals(works.works[1].poet, "")
        self.assertEquals(works.works[2].poet, "")
        self.assertEquals(works.works[3].poet, "Francesco Petrarca")

        self.assertEquals(works.works[0].part, 1)
        self.assertEquals(works.works[1].part, 1)
        self.assertEquals(works.works[2].part, 2)
        self.assertEquals(works.works[3].part, 1)

        self.assertEquals(works.works[0].page, 1)
        self.assertEquals(works.works[1].page, 2)
        self.assertEquals(works.works[2].page, 3)
        self.assertEquals(works.works[3].page, 4)

        self.assertEquals(works.works[0].composer, "Default Composer")
        self.assertEquals(works.works[1].composer, "New Composer")
        self.assertEquals(works.works[2].composer, "New Composer")
        self.assertEquals(works.works[3].composer, "Default Composer")

