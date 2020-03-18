from glob import glob
import os
import shutil
base_path = "H:\\Bengali NLP\\Books Images"
folders = glob(base_path + '/*/')

for folder in folders:
    image_path = folder + "Images"
    if not os.path.isdir(image_path):
        os.mkdir(image_path)

    if not os.path.isdir(folder + "Text"):
        os.mkdir(folder + "Text")
    
    images = folder + "\\*.jpg"

    for idx, image in enumerate(glob(images), start = 1):
        new_file =  image_path + "\\" + f"{idx}.jpg"
        shutil.move(image, new_file)