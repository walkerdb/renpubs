import os
from tqdm import tqdm
from PIL import Image


def main():
    root_path = "/Volumes/Samsung USB/nv images/data"
    images = [image for image in os.listdir(root_path) if image.endswith(".tif") and not image.startswith(".")]
    images.sort()

    for index, image in enumerate(tqdm(images)):
        image_path = os.path.join(root_path, image)
        image = Image.open(image_path)
        new_size = (int(s * 0.5) for s in image.size)
        image.resize(new_size, Image.BICUBIC)

        image.save(os.path.join(root_path, "{:04d}.png").format(index + 1))


def crop_images(start, end):
    path_template = "/Volumes/Samsung USB/nv images/out/{}.png"
    for i in tqdm(range(start, end)):
        name = str(i).zfill(4)
        try:
            image = Image.open(path_template.format(name))

            width, height = image.size  # Get dimensions

            new_width = width * 0.70
            new_height = height * 0.70

            left = (width - new_width) / 2
            top = (height - new_height) / 2
            right = (width + new_width) / 2
            bottom = (height + new_height) / 2

            image = image.crop((left, top, right, bottom))

            image.save("/Volumes/Samsung USB/crops/{}.png".format(name))
        except:
            print("failed to crop image {}.png".format(name))
            continue


if __name__ == "__main__":
    crop_images(1127, 1952)
    # main()
