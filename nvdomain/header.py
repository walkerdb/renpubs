import re

from nvdomain.constants import LOCATIONS, PRINTERS, ITALIAN_NUMBERS, ITALIAN_NUMBERS_ORDINAL, MUSIC_GENRES
from nvdomain.spelling import OldToModernSpellingPair


def normalize_name(composer):
    caps_name = re.findall("([A-ZÈÉÌÍÁÙÚÜ ]*?) [A-Z][a-zéèîìáùúü]", composer)[0]

    name_without_caps_part = composer.replace(caps_name, "").strip()
    return "{} {}".format(name_without_caps_part, caps_name.title())


class Header(object):
    def __init__(self, header):
        self.process_title_data(header)

    def process_title_data(self, header):
        number, composer_and_year, title = re.match(r"(\d{1,4}(?: bis)?) -? ?(.*?\)) (.*)", header).groups()

        year_string, year = self.extract_year(composer_and_year)

        self.number = number
        self.title = self.clean_title(title)
        self.year = year
        self.composers = self.extract_composers(composer_and_year.replace(year_string, ""))
        self.printing_location = self.extract_printing_location()
        self.printers = self.extract_printer()
        self.voices = self.extract_voices()
        self.book_number = self.extract_book_number()
        self.genres = self.extract_genres()

    @staticmethod
    def clean_title(title):
        return title.strip("- ")

    @staticmethod
    def extract_year(composer):
        return re.findall(r"(\((\d{4}).*\))", composer)[0]

    @staticmethod
    def extract_composers(composer):
        composers = composer.strip().split(" - ")
        return [normalize_name(composer) for composer in composers]

    def extract_printing_location(self):
        matching_locations = [OldToModernSpellingPair(old, modern) for old, modern in LOCATIONS.items() if old.lower() in self.title.lower()]

        if not matching_locations:
            return self.get_default_printing_location_from_printer()

        if len(matching_locations) > 1:
            return self.get_last_matching_location(matching_locations)

        return matching_locations[-1]

    def get_default_printing_location_from_printer(self):
        printers = sorted([printer for name, printer in PRINTERS.items() if name in self.title])
        if not printers:
            print("no matching printing locations: ", self.title)
            return ""
        return OldToModernSpellingPair("LOCATION_NOT_PRESENT_IN_ORIGINAL", printers[0].primary_location)

    def get_last_matching_location(self, matching_locations):
        highest_index = 0
        winning_location = ""
        for location in matching_locations:
            index = self.title.index(location.original)
            if index > highest_index:
                highest_index = index
                winning_location = location
        return winning_location

    def extract_printer(self):
        return [OldToModernSpellingPair(name, printer.name) for name, printer in PRINTERS.items() if name.lower() in self.title.lower()]

    def extract_voices(self):
        return self.extract_english_terms_from_italian_title_with_mapping(ITALIAN_NUMBERS)

    def extract_book_number(self):
        book_number = self.extract_english_terms_from_italian_title_with_mapping(ITALIAN_NUMBERS_ORDINAL)
        if book_number:
            return book_number[0]

        print("no book number found")
        return None

    def extract_genres(self):
        return self.extract_english_terms_from_italian_title_with_mapping(MUSIC_GENRES)

    def extract_english_terms_from_italian_title_with_mapping(self, mapping):
        return sorted([eng_term for it_term, eng_term in mapping.items() if it_term.lower() in self.title.lower()])








