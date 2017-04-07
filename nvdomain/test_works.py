from unittest import TestCase

from nvdomain.works import Works


class TestWorks(TestCase):
    def test_basic_works_processing(self):
        works = Works(
            "A 4. In mio dulce dolores (Petrarca) 1\n"
            '" " Amo Amas I Love a Lass (seconda parte) " 2\n'
            'A 5. Yo check it (di Walker) 3',
            4,
            "Arcadelt"
        )
        self.assertEquals(works.works[0].voices, "4")
        self.assertEquals(works.works[1].voices, "4")
        self.assertEquals(works.works[2].voices, "5")

        self.assertEquals(works.works[0].title, "In mio dulce dolores")
        self.assertEquals(works.works[1].title, "Amo Amas I Love a Lass")
        self.assertEquals(works.works[2].title, "Yo check it")

        self.assertEquals(works.works[0].poet, "Petrarca")
        self.assertEquals(works.works[1].poet, "Petrarca")
        self.assertEquals(works.works[2].poet, "")

        self.assertEquals(works.works[0].part, 1)
        self.assertEquals(works.works[1].part, 2)
        self.assertEquals(works.works[2].part, 1)

        self.assertEquals(works.works[0].composer, "Arcadelt")
        self.assertEquals(works.works[1].composer, "Arcadelt")
        self.assertEquals(works.works[2].composer, "Walker")
