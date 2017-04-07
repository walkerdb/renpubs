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
    def __init__(self):
        self.works = []
        self.dedication = Dedication()
        self.book_data = BookData()
        self.title = ""
        self.year = ""
        self.main_composer = ""
        self.voices = []
        self.genres = []
        self.nv_number = ""
        self.locations = []