import os
from tqdm import tqdm
from PIL import Image

root_path = "/Volumes/Samsung USB/nv images/out"
images = [image for image in os.listdir(root_path) if image.endswith(".tif") and not image.startswith(".")]
images.sort()

for index, image in enumerate(tqdm(images)):
    image_path = os.path.join(root_path, image)
    image = Image.open(image_path)
    new_size = (int(s * 0.5) for s in image.size)
    image.resize(new_size, Image.BICUBIC)

    image.save(os.path.join(root_path, "{:04d}.png").format(index + 1))
