from nvdomain.semi_structured.work import Work
from util.field_equality_mixin import FieldEqualityMixin


class Works(FieldEqualityMixin):
    def __init__(self, works, default_voices, default_composer):
        works = [w for w in works.strip("\n").split("\n") if w]

        self.works = []
        context = {
            "prev_text": "",
            "current_voices": default_voices,
            "current_poet": "",
            "default_composer": default_composer
        }
        for work_text in works:
            work = Work(work_text, context)

            context["prev_text"] = work_text
            context["current_poet"] = work.poet
            context["current_voices"] = work.voices

            self.works.append(work)
