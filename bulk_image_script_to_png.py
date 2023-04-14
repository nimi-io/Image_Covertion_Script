import sys
import os
from PIL import Image, ImageFilter
# python3 bulk_image_script_to_png.py pokedex/ newdex/ --------to run
# grab first argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]
print(image_folder, output_folder)
# check if new folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through firs argumen and converte images to png
for file_name in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{file_name}').filter(ImageFilter.SHARPEN)
    print(img)
    img.save(f'{output_folder}{os.path.splitext(file_name)[0]}.png', 'png')

print("all done")
