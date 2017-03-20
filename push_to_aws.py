import subprocess
import os
from tqdm import tqdm

root_path = "/Volumes/Samsung USB/nv images/out"
images = [image for image in os.listdir(root_path) if image.endswith(".png") and not image.startswith(".")]
images.sort()

print(images)

for image in tqdm(images):
    path = os.path.join(root_path, image)
    aws_path = "s3://earlyaudio/nv/{}".format(image)

    process = subprocess.Popen(
        ["aws", "s3", "cp", path, aws_path],
        shell=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    process.wait()
