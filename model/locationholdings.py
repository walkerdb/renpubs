class Publication(object):

    def __init__(self):
        self.works = []
        self.dedication = {
            "year": "",
            "dedicator": "",
            "dedicatee": "",
            "location": "",
            "text": "",
        }
        self.title = ""
        self.year = ""
        self.main_composer = ""
        self.voices = []
        self.genres = []
        self.nv_number = ""
        self.locations = []
