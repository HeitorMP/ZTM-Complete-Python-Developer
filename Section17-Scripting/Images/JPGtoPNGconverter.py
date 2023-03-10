from PIL import Image, ImageFilter
import sys
import os


try:
    src_folder = sys.argv[1]
    if not os.path.exists(src_folder):
        print('Invalid path!')
        exit(1)
    dest_folder = sys.argv[2]
except IndexError as err:
    print('Invalid params!')
    exit(1)


if not os.path.exists(dest_folder):
    try:
        os.mkdir(dest_folder)
    except PermissionError as err:
        print("Impossible to create!")
        exit(1)

file_list = [file for file in os.listdir(src_folder) if file.endswith('.jpg')]

for file in file_list:
    img = Image.open(src_folder + '/' + file)
    img.save(dest_folder + '/' + file[:-3] + 'png', "png")
