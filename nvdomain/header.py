import re

from nvdomain.constants import LOCATIONS, PRINTERS, ITALIAN_NUMBERS, ITALIAN_NUMBERS_ORDINAL, MUSIC_GENRES
from util.extraction import extract_location
from util.field_equality_mixin import FieldEqualityMixin
from util.spelling import OldToModernSpellingPair


def normalize_name(composer):
    if "dalla Viola" in composer:
        return "Alfonso dalla Viola"
    if "Flandrus" in composer:
        return "Arnoldus Flandrus"

    caps_name = re.findall("([A-ZÈÉÌÍÁÙÚÜ ']*?) [A-Zd]['a-zéèîìáùúü]", composer)[0]

    name_without_caps_part = composer.replace(caps_name, "").strip()
    return "{} {}".format(name_without_caps_part, caps_name.title())


class Header(FieldEqualityMixin):
    def __init__(self, header):
        number, composer_and_year, title = re.match(r"(\d{1,4}(?: bis)?) -? ?(.*?\)) (.*)", header).groups()
        year_string, year = self.extract_year(composer_and_year)

        self.number = number
        self.title = self.clean_title(title)
        self.year = year
        self.year_index = year_string
        self.composers = self.extract_composers(composer_and_year.replace(year_string, ""))
        self.printing_location = self.extract_location(title)
        self.printers = self.extract_printer(title)
        self.voices = self.extract_voices(title)
        self.book_number = self.extract_book_number(title)
        self.genres = self.extract_genres(title)

    @staticmethod
    def clean_title(title):
        return title.strip("- ")

    @staticmethod
    def extract_year(composer_year_text):
        return re.findall(r"(\((\d{4}).*\))", composer_year_text)[0]

    @staticmethod
    def extract_composers(composer):
        composers = composer.strip().split(" - ")
        return [normalize_name(composer) for composer in composers]

    @staticmethod
    def extract_location(title):
        matching_location = extract_location(title)

        if not matching_location:
            return Header.get_default_printing_location_from_printer(title)

        return matching_location

    @staticmethod
    def get_default_printing_location_from_printer(title):
        printers = sorted([printer for name, printer in PRINTERS.items() if name in title])
        if not printers:
            return OldToModernSpellingPair("NO_PRINTER_KNOWN", "NO_PRINTER_KNOWN")

        return OldToModernSpellingPair("LOCATION_NOT_PRESENT_IN_ORIGINAL", printers[0].primary_location)

    @staticmethod
    def extract_printer(title):
        printers = [OldToModernSpellingPair(name, printer.name) for name, printer in sorted(PRINTERS.items()) if name in title]
        if not printers:
            print("no known printers found: ", title)
            return [OldToModernSpellingPair("NO_PRINTER_KNOWN", "NO_PRINTER_KNOWN")]

        return printers

    @staticmethod
    def extract_voices(title):
        return Header.extract_english_terms_from_italian_title_with_mapping(ITALIAN_NUMBERS, title)

    @staticmethod
    def extract_book_number(title):
        book_number = Header.extract_english_terms_from_italian_title_with_mapping(ITALIAN_NUMBERS_ORDINAL, title)

        if not book_number:
            return 1

        return book_number[0]

    @staticmethod
    def extract_genres(title):
        return Header.extract_english_terms_from_italian_title_with_mapping(MUSIC_GENRES, title)

    @staticmethod
    def extract_english_terms_from_italian_title_with_mapping(mapping, title):
        return sorted(list({eng_term for it_term, eng_term in mapping.items() if it_term.lower() in title.lower()}))

    def get_default_composer(self):
        return self.composers[0] if len(self.composers) > 0 else ""

    def get_default_voices(self):
        return self.voices[0] if len(self.voices) > 0 else ""
