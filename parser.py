import os
from pprint import pprint

import re

from nvdomain import Header


def main(start, end):
    texts = extract_texts(end, start)

    publications = re.split(r"\n\n\n\n+", texts)
    for publication in publications:
        _header, meta, works, locations = extract_sections(publication)
        # print(_header)

        header = Header(_header)

        print(header.composers[0])

        # normalize composer name

        # parse metadata string
        # parse works string
        # parse locations string



def process_title_data(title):
    number, composer, title = re.match(r"(\d{1,4}(?: bis)?) -? ?(.*?\)) (.*)", title).groups()

    title = title.strip("- ")

    year_string, year = re.findall(r"(\((\d{4}).*\))", composer)[0]
    composer = composer.replace(year_string, "").strip()

    print(composer)

    return number, composer, title


def extract_sections(publication):
    data = publication.strip("\n").split("\n\n")
    title = meta = works = locations = ""

    if len(data) is 3:
        title, meta, locations = data

    elif len(data) is 4:
        title, meta, works, locations = data

    else:
        pass

    title = title.replace("\n", " ")

    return title, meta, works, locations


def extract_texts(end, start):
    texts = ""
    files = os.listdir("out")
    for file in files[start - 1:end]:
        with open(os.path.join("out", file)) as f:
            texts += "\n" + f.read().rstrip("\n ")
    return texts


if __name__ == "__main__":
    main(9, 140)
