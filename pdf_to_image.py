# from pdf2image import convert_from_path, convert_from_bytes
# from glob import glob
# import os
# output_path = "H:/Bengali NLP/Books Images/BanglaSahitto"
# images_from_path = convert_from_path('H:/Board Books/Bangla Sahitto.pdf', output_folder=output_path, fmt='jpg', grayscale=True)
# for idx, file in enumerate(glob(output_path + "/*.jpg"), start=1):
#     new_file = output_path + f"/{idx}.jpg"
#     os.rename(file, new_file)


from pdf2image import convert_from_path, convert_from_bytes
from glob import glob
import os
output_path = "H:/Multiple/Images"
#images_from_path = convert_from_path('H:/Mutiple_MMRS_Updated.pdf', output_folder=output_path, fmt='jpg', grayscale=True)

for idx, file in enumerate(glob(output_path + "/*.jpg"), start=1):
    new_file = output_path + f"/{idx}.jpg"
    os.rename(file, new_file)




