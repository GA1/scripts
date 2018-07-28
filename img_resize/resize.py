import PIL
from PIL import Image

NUMNBER_OF_PIXELS_ON_RESIZED_IMAGE = 1024 * 1024 * 2
image_extensions = ['.png', '.jpg', 'jpeg', '.bmp', ]

mywidth = 300


def is_image_file_name(file_name):
    file_name=file_name.lower()
    for extension in image_extensions:
        if file_name.endswith(extension):
            return True
    return False


import os

input_directory = "./input/"
for file_name in os.listdir(input_directory):
    print(1111111)
    print(file_name)
    if is_image_file_name(file_name):
        img = Image.open(input_directory + file_name)
        # wpercent = (mywidth / float(img.size[0]))
        # hsize = int((float(img.size[1]) * float(wpercent)))
        print (img.size[0], img.size[1])
        # img = img.resize((mywidth, hsize), PIL.Image.ANTIALIAS)
        img.save('./output/resized.jpg')
        print(os.path.join("/output", file_name))
#
# img = Image.open('someimage.jpg')
# wpercent = (mywidth / float(img.size[0]))
# hsize = int((float(img.size[1]) * float(wpercent)))
# img = img.resize((mywidth, hsize), PIL.Image.ANTIALIAS)
# img.save('resized.jpg')
