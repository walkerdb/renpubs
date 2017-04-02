import io
import os

from google.cloud import vision

vision_client = vision.Client(project="text-detection-161223")

file_name = os.path.join(os.path.dirname(__file__), '/Users/walkerdb/Downloads/IMG_4062_2R.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()
    image = vision_client.image(
        content=content)

# Performs label detection on the image file
texts = image.detect_text()

for text in texts:
    print(text.description)
    for vertex in text.bounds.vertices:
        print(vertex.x_coordinate)
        print(vertex.y_coordinate)
