import os
from collections import Counter
from pprint import pprint

import re

import jsonpickle

from nvdomain.description import Description
from nvdomain.header import Header
from nvdomain.librarylocations import LibraryLocations
from nvdomain.nventry import NvEntry
from nvdomain.works import Works


def main(start, end):
    counts = []
    texts = extract_texts(end, start)

    publications = re.split(r"\n\n\n\n+", texts)
    for publication in publications:
        nv_entry = NvEntry(publication)

        pprint(jsonpickle.json.loads(
            jsonpickle.dumps(nv_entry, unpicklable=False))
        )
        counts.extend([work.composer for work in nv_entry.works.works])
        # print(header.composers[0])

        # parse metadata string
        # parse works string
        # parse locations string


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
