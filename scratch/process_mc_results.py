import csv


with open("/Users/walkerdb/Downloads/Batch_3337169_batch_results.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        img = row["Input.image_url"]
        page = img.replace(".png", "").replace("https://earlyaudio.s3.amazonaws.com/nv/", "")
        with open("../input_output/data/{}.txt".format(page), mode="w") as ff:
            ff.write(row["Answer.text"])
