import colander


class Publication(object):
    def __init__(self, nv_entry):
        self.title = nv_entry.header.title
        self.identifiers = {"nuovo_vogel": nv_entry.header.number}
        self.year = nv_entry.header.year
        self.composers = nv_entry.header.composers,
        self.printing_info = {
            "printers": nv_entry.header.printers,
            "location": nv_entry.header.printing_location.modern
        }
        self.genres = nv_entry.header.genres
        self.voices = nv_entry.header.voices
        self.physical_description = nv_entry.description.book_details
        self.dedication = nv_entry.description.dedication
        self.works = nv_entry.works.works
        self.library_locations = nv_entry.library_locations.libraries

        example_output = {
            "title": "",
            "year": "",
            "composers": [],
            "printing_info": {
                "printers": [],
                "location": ""  # modern
            },
            "genres": [],
            "series_number": 0, # primo, secondo, etc
            "voices": [], # iterate over works
            "physical_description": {
                "number_of_books": 0,
                "book_size": "Quarto",
                "pages": 0,
                "is_oblong": bool
            },
            "dedication": {
                "text": "",
                "dedicator": "",
                "dedicatee": "",
                "location": ""
            },
            "works": [{
                "title": "",
                "composer": "",
                "voices": 0,
                "poet": "",
                "part": 0,
            }],
            "library_locations": [{"siglum": "", "parts": ""}],
            "identifiers": {
                "nuovo_vogel": "1"
            }
        }
