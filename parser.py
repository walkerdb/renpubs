import os
from pprint import pprint

import re

import jsonpickle

from domain.formattedoutput import FormattedOutput
from nvdomain.nventry import NvEntry


def main(start, end):
    texts = extract_texts(end, start)
    publications = re.split(r"\n\n\n\n+", texts)
    entries = [NvEntry(pub) for pub in publications]
    output = FormattedOutput(entries)
    pprint(jsonpickle.json.loads(jsonpickle.dumps(output.publications[0], unpicklable=False)))


def extract_texts(end, start):
    texts = ""
    files = os.listdir("input_output/data")
    for file in files[start - 1:end]:
        with open(os.path.join("input_output/data", file)) as f:
            texts += "\n" + f.read().rstrip("\n ")
    return texts


if __name__ == "__main__":
    main(9, 140)
