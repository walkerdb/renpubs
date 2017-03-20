import subprocess
import os
from tqdm import tqdm

root_path = "/Volumes/Samsung USB/nv images/out"
images = [image for image in os.listdir(root_path) if image.endswith(".tif")]

for image in tqdm(images):
    input_path = os.path.join(root_path, image)
    output_path = "out/" + image.split(".")[0]

    process = subprocess.Popen(
        ["tesseract", input_path, output_path, "--psm", "4", "-l", "ita_old+ita+fra+ger"],
        shell=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    process.wait()
