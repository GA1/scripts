import argparse
import os
import PIL
from PIL import Image
from math import sqrt

parser = argparse.ArgumentParser()
parser.add_argument('-m', metavar="mega_pixels", help="Number of Megapixels", type=float, required=False, default=4)

args = parser.parse_args()
NUMBER_OF_MEGA_PIXELS = args.m
NUMBER_OF_PIXELS_ON_RESIZED_IMAGE = 1024 * 1024 * NUMBER_OF_MEGA_PIXELS
image_extensions = ['.png', '.jpg', 'jpeg', '.bmp', ]
input_directory = "./input/"
output_directory = "./output/"


def is_image_file_name(file_name):
    file_name = file_name.lower()
    for extension in image_extensions:
        if file_name.endswith(extension):
            return True
    return False


def resize(img):
    original_width = img.size[0]
    original_height = img.size[1]
    number_of_pixels_before_resizing = original_width * original_height
    factor_of_resizing = number_of_pixels_before_resizing / NUMBER_OF_PIXELS_ON_RESIZED_IMAGE
    sqrt_of_factor_of_resizing = sqrt(factor_of_resizing)
    new_width = int(original_width / sqrt_of_factor_of_resizing)
    new_height = int(original_height / sqrt_of_factor_of_resizing)
    img = img.resize((new_width, new_height), PIL.Image.ANTIALIAS)
    return img


image_file_names = list(filter(is_image_file_name, os.listdir(input_directory)))
N = len(image_file_names)
i = 1
for image_file_name in image_file_names:
    print('[' + str(i)  + '/' + str(N) + '] ' + 'resizing the image: ' + image_file_name)
    img = Image.open(input_directory + image_file_name)
    img = resize(img)
    img.save(output_directory + image_file_name.lower())
    i = i + 1
print('RESIZING DONE')

