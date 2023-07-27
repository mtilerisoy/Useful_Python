import os
from PIL import Image

def compress(image_file, quality):

    filepath = os.path.join(os.getcwd(), image_file)

    image = Image.open(filepath)

    image.save("image-file-compressed",
                 "JPEG",
                 optimize = True,
                 quality = quality)
    return

compress("file/path", 65)