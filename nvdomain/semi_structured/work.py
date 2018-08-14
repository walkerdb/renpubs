import re
from pprint import pprint

from util.field_equality_mixin import FieldEqualityMixin

part_to_num_dict = {
    "seconda ": 2,
    "terza ": 3,
    "quarta ": 4,
    "quinta ": 5,
    "sesta ": 6,
    "settima ": 7,
    "ottava ": 8,
    "nona ": 9,
    "decima ": 10,
    "undicesima ": 11,
    "dodicesima ": 12,
    "tredicesima ": 13,
    "quattordicesima ": 14,
}


class Work(FieldEqualityMixin):
    def __init__(self, text, context):
        split_text = [n for n in text.split("\t") if n]
        voices, title, notes, composer, poet, page = [t.strip(" -") for t in split_text]

        self.voices = self.find_voices(voices) if voices else context["current_voices"]
        self.title = title.lstrip("123456789. ")
        self.poet = poet
        self.part = self.extract_part("({})".format(notes).lower())
        self.composer = composer if composer else context["default_composer"]
        self.page = int(page) if page else -1

    @staticmethod
    def find_voices(text):
        try:
            return int(re.findall(r"^A (\d\d?)|$", text)[0])
        except ValueError:
            return ""

    @staticmethod
    def extract_part(text):
        parentheticals = [s for s in re.findall(r"\(([^()]*?)\)|$", text) if "parte" in s]
        for parenthetical in parentheticals:
            for parte, number in part_to_num_dict.items():
                if parte in parenthetical:
                    return number
        return 1
