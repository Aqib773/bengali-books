import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import os
from glob import glob
input_path = "H:\\Bengali NLP\\Books Images\\Ovidhan\\Images\\"

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'


for idx in range(231, 1455):
    image = Image.open(input_path + f"{idx}.jpg")
    text = pytesseract.image_to_string(image, lang="ben", config=tessdata_dir_config)
    with open(f'H:/Bengali NLP/Books Images/Ovidhan/Text/{idx}.txt', mode='w', encoding='utf-8-sig') as output_file:
        output_file.write(text)
        print(f"{idx} done")

        