import colander


class LibraryHoldings(object):
    def __init__(self):
        self.code = ""
        self.parts = []


class Dedication(object):
    def __init__(self):
        self.year = ""
        self.dedicator = ""
        self.dedicatee = ""
        self.location = ""
        self.text = ""


class Work(object):
    def __init__(self):
        self.title = ""
        self.num_voices = ""
        self.comment = ""
        self.part = ""
        self.composer = ""
        self.poet = ""
        self.page = ""


class BookData(object):
    def __init__(self):
        self.num_books = ""
        self.pages = ""
        self.format = ""


class Publication(object):
    def __init__(self, nv_entry):
        self.title = nv_entry.header.title
        self.year = nv_entry.header.year
        self.composers = nv_entry.header.composers,
        self.printing_info = {
            "printers": nv_entry.header.printers,
            "location": nv_entry.header.printing_location.modern
        }
        self.genres = nv_entry.header.genres
        self.series_number = nv_entry.header.number
        self.voices = nv_entry.header.voices
        self.book_info = nv_entry.description.book_details
        self.dedication = nv_entry.description.dedication
        self.works = nv_entry.works.works
        self.library_locations = nv_entry.library_locations

        x = {
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
            "book_info": {
                "number_of_books": 0,
                "book_size": "Quarto",
                "pages": 0,
                "is_oblong": bool
            },
            "catalog_numbers": {
                "nv": "",
                "RISM": ""
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
            },],
            "library_locations": [{"siglum": "", "parts": ""},]

        }