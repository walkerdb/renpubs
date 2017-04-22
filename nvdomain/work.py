import re

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
        voices = self.find_voices(text)
        self.voices = voices if voices else context["current_voices"]
        self.title = self.extract_title(text)
        self.poet = self.extract_poet(text, context)
        self.part = self.extract_part(text)
        self.composer = self.extract_composer(text, context)

    @staticmethod
    def find_voices(text):
        try:
            return int(re.findall(r"^A (\d\d?)|$", text)[0])
        except ValueError:
            return ""

    @staticmethod
    def extract_title(text):
        return re.sub(r"^A \d\d?\.?|\(.*?\)|\d{1,4}$", "", text).strip(" \".,")

    @staticmethod
    def extract_poet(text, context):
        strip_text = text.rstrip("1234567890 \".,")
        parenthetical = re.findall(r"\(([^()]*?)\)$|$", strip_text)[0]

        if parenthetical.startswith("di ") or " parte" in parenthetical:
            return Work.get_default_poet_if_ditto_mark(text, context)

        return parenthetical

    @staticmethod
    def get_default_poet_if_ditto_mark(text, context):
        return context.get("current_poet") if re.search(r' " | "$', text) else ""

    @staticmethod
    def extract_part(text):
        parentheticals = [s for s in re.findall(r"\(([^()]*?)\)|$", text) if "parte" in s]
        for parenthetical in parentheticals:
            for parte, number in part_to_num_dict.items():
                if parte in parenthetical:
                    return number
        return 1

    @staticmethod
    def extract_composer(text, context):
        composer = re.findall(r"\(di ([^)]*?)\)|$", text)[0]
        return composer if composer else context.get("default_composer")


