import os
import re
import json

import jsonpickle

from domain.formattedoutput import FormattedOutput
from nvdomain.nventry import NvEntry
from nvdomain.semi_structured.semi_structured_work import SemiStructuredWorkParser


def parse_works_from_page_transcripts(start, end):
    texts = extract_texts(end, start)
    publications = re.split(r"\n\n\n\n+", texts)
    entries = []
    for pub in publications:
        try:
            entries.append(NvEntry(pub, entries.copy()))
        except:
            print(pub)
            exit()

    # entries = [NvEntry(pub) for pub in publications]

    # questionable_entries = [entry for entry in entries if len(entry.library_locations.libraries) > 9]
    # print("questionable entries:")
    # pprint(json.loads(jsonpickle.dumps(questionable_entries, unpicklable=False)))

    return FormattedOutput(entries)


def parse_works_from_old_style_tables():
    root_dir = "input_output/old_files"
    raw_publications = []

    dirs = sorted([f for f in os.listdir(root_dir) if not f.startswith(".") and not f.startswith("0000")])
    for filepath in dirs:
        with open(os.path.join("input_output/old_files", filepath), mode="r") as f:
            raw_publications.append(f.read())

    parsed_publications = []
    for pub in raw_publications:
        parsed_publications.append(SemiStructuredWorkParser(pub, parsed_publications.copy()))

    return FormattedOutput(parsed_publications)


def extract_texts(end, start):
    texts = ""
    files = sorted(os.listdir("input_output/data"))

    for file in files[start - 1:end]:
        with open(os.path.join("input_output/data", file)) as f:
            texts += "\n" + f.read().rstrip("\n ")
    return texts


if __name__ == "__main__":
    first_page_with_works = 9
    last_page_to_process = 217

    output = parse_works_from_page_transcripts(first_page_with_works, last_page_to_process)
    output.publications.extend(parse_works_from_old_style_tables().publications)

    with open("publications.json", mode="w") as f:
        json.dump(
            json.loads(jsonpickle.dumps(output.publications, unpicklable=False)),
            f, indent=2, sort_keys=True, ensure_ascii=False
        )

    with open("README.md", mode="r") as f:
        text = f.read()
        text = re.sub("Current publication count: \d+", "Current publication count: {}".format(len(output.publications)), text)
        text = re.sub("Total works: \d+", "Total works: {}".format(sum([len(p.works) for p in output.publications])), text)

    with open("README.md", mode="w") as f:
        f.write(text)
