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
        self.assertEquals(works.works[0].voices, 4)
        self.assertEquals(works.works[1].voices, 4)
        self.assertEquals(works.works[2].voices, 5)

        self.assertEquals(works.works[0].title, "In mio dulce dolores")
        self.assertEquals(works.works[1].title, "Amo Amas I Love a Lass")
        self.assertEquals(works.works[2].title, "Yo check it")

        self.assertEquals(works.works[0].poet, "Petrarca")
        self.assertEquals(works.works[1].poet, "Petrarca")
        self.assertEquals(works.works[2].poet, "")

        self.assertEquals(works.works[0].part, 1)
        self.assertEquals(works.works[1].part, 2)
        self.assertEquals(works.works[2].part, 1)

        self.assertEquals(works.works[0].page, 1)
        self.assertEquals(works.works[1].page, 2)
        self.assertEquals(works.works[2].page, 3)

        self.assertEquals(works.works[0].composer, "Arcadelt")
        self.assertEquals(works.works[1].composer, "Arcadelt")
        self.assertEquals(works.works[2].composer, "Walker")

    def test_handles_composer_poet_part_interactions(self):
        works = Works(
            'A 5. Has voices, composer, and poet (Di Composer) (The Poet) 1\n'
            '" " Has ditto voices, composer, part, and ditto poet (seconda parte) (Di Composer) " 2\n'
            '" " Has ditto voices, composer, part, and no poet (terza parte) (Di Composer) 3',
            4,
            "Arcadelt"
        )

        first_work = works.works[0]
        second_work = works.works[1]
        third_work = works.works[2]

        self.assertEquals(first_work.voices, 5)
        self.assertEquals(second_work.voices, 5)
        self.assertEquals(third_work.voices, 5)

        self.assertEquals(first_work.title, "Has voices, composer, and poet")
        self.assertEquals(second_work.title, "Has ditto voices, composer, part, and ditto poet")
        self.assertEquals(third_work.title, "Has ditto voices, composer, part, and no poet")

        self.assertEquals(first_work.poet, "The Poet")
        self.assertEquals(second_work.poet, "The Poet")
        self.assertEquals(third_work.poet, "")

        self.assertEquals(first_work.part, 1)
        self.assertEquals(second_work.part, 2)
        self.assertEquals(third_work.part, 3)

        self.assertEquals(first_work.page, 1)
        self.assertEquals(second_work.page, 2)
        self.assertEquals(third_work.page, 3)

        self.assertEquals(first_work.composer, "Composer")
        self.assertEquals(second_work.composer, "Composer")
        self.assertEquals(third_work.composer, "Composer")
