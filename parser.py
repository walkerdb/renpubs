import os
from pprint import pprint

import re


def main(start, end):
    texts = extract_texts(end, start)

    publications = re.split(r"\n\n\n\n+", texts)
    for publication in publications:
        title, meta, works, locations = extract_sections(publication)

        title = title.replace("\n", " ")

        number, composer, title = re.match(r"(\d{1,4}(?: bis)?) -? ?(.*?\)) (.*)", title).groups()
        title = title.strip("- ")
        try:
            print(title)
        except AttributeError as e:
            print(title)


def extract_sections(publication):
    data = publication.strip("\n").split("\n\n")
    title = meta = works = locations = ""

    if len(data) is 3:
        title, meta, locations = data

    elif len(data) is 4:
        title, meta, works, locations = data

    else:
        pass

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
