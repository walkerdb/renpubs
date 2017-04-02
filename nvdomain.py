import re


def normalize_name(composer):
    caps_name = re.findall("([A-ZÈÉÌÍÁÙÚÜ ]*?) [A-Z][a-zéèîìáùúü]", composer)[0]

    name_without_caps_part = composer.replace(caps_name, "").strip()
    return "{} {}".format(name_without_caps_part, caps_name.title())


class Header(object):
    def __init__(self, header):
        number, composers, title, year = self.process_title_data(header)

        self.title = title
        self.number = number
        self.composers = composers
        self.year = year

    @staticmethod
    def process_title_data(header):
        number, composer, title = re.match(r"(\d{1,4}(?: bis)?) -? ?(.*?\)) (.*)", header).groups()

        title = title.strip("- ")

        year_string, year = re.findall(r"(\((\d{4}).*\))", composer)[0]
        composer = composer.replace(year_string, "").strip()
        composers = composer.split(" - ")

        composers = [normalize_name(composer) for composer in composers]

        return number, composers, title, year


class Description(object):
    def __init__(self, description):
        pass


class Works(object):
    def __init__(self, works):
        pass