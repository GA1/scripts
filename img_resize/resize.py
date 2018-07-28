import os
import PIL
from PIL import Image
from math import sqrt

NUMBER_OF_MEGA_PIXELS = 8
NUMNBER_OF_PIXELS_ON_RESIZED_IMAGE = 1024 * 1024 * NUMBER_OF_MEGA_PIXELS
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
    factor_of_resizing = number_of_pixels_before_resizing / NUMNBER_OF_PIXELS_ON_RESIZED_IMAGE
    sqrt_of_factor_of_resizing = sqrt(factor_of_resizing)
    new_width = int(original_width / sqrt_of_factor_of_resizing)
    new_height = int(original_height / sqrt_of_factor_of_resizing)
    img = img.resize((new_width, new_height), PIL.Image.ANTIALIAS)
    return img


for file_name in os.listdir(input_directory):
    if is_image_file_name(file_name):
        img = Image.open(input_directory + file_name)
        img = resize(img)
        img.save(output_directory + file_name.lower())