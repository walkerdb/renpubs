import os
import csv


def main():
    url_template = "https://earlyaudio.s3.amazonaws.com/nv/{}.png"
    csv_rows = []
    for page in range(174, 200):
        qualified_page = str(page).zfill(4)
        url = url_template.format(qualified_page)
        with open("../input_output/data/{}.txt".format(qualified_page), mode="r") as f:
            text = f.read()

        csv_rows.append([text, url])


    with open("mc_output.csv", mode="w") as f:
        writer = csv.writer(f)
        writer.writerow(["text", "image_url"])
        writer.writerows(csv_rows)

    pass


if __name__ == "__main__":
    main()
