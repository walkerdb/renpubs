import os
from pprint import pprint

import re
import json

import jsonpickle

from domain.formattedoutput import FormattedOutput
from nvdomain.nventry import NvEntry


def main(start, end):
    texts = extract_texts(end, start)
    publications = re.split(r"\n\n\n\n+", texts)
    entries = [NvEntry(pub) for pub in publications]

    questionable_entries = [entry for entry in entries if len(entry.library_locations.libraries) > 9]
    pprint(json.loads(jsonpickle.dumps(questionable_entries, unpicklable=False)))

    output = FormattedOutput(entries)

    with open("publications.json", mode="w") as f:
        json.dump(json.loads(jsonpickle.dumps(output.publications, unpicklable=False)), f, indent=2, sort_keys=True, ensure_ascii=False)


def extract_texts(end, start):
    texts = ""
    files = os.listdir("input_output/data")
    for file in files[start - 1:end]:
        with open(os.path.join("input_output/data", file)) as f:
            texts += "\n" + f.read().rstrip("\n ")
    return texts


if __name__ == "__main__":
    main(9, 140)
