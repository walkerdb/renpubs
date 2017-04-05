from nvdomain.constants import LOCATIONS
from util.spelling import OldToModernSpellingPair


def extract_location(text):
    matching_locations = [OldToModernSpellingPair(old, modern) for old, modern in LOCATIONS.items() if old in text]

    if not matching_locations:
        ""

    if len(matching_locations) > 1:
        return get_last_matching_location(matching_locations, text)

    return matching_locations[0]


def get_last_matching_location(matching_locations, text):
    highest_index = 0
    winning_location = ""
    for location in matching_locations:
        try:
            index = text.index(location.original)
        except:
            print(location.original)
            print(text)
            exit()
        if index > highest_index:
            highest_index = index
            winning_location = location
    return winning_location
