import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import os
from glob import glob
input_path = "H:\\Multiple\\Images\\"

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'


for idx in range(1, 11):
    image = Image.open(input_path + f"{idx}.jpg")
    text = pytesseract.image_to_string(image, lang="eng", config=tessdata_dir_config)
    with open(f'H:\\Multiple\\Text\\{idx}.txt', mode='w', encoding='utf-8-sig') as output_file:
        output_file.write(text)
        print(f"{idx} done")

        