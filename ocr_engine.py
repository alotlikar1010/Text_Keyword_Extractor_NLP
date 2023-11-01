import pytesseract # this library is used for optical character regonation OCR to extract text from images
from PIL import Image
import os




class OCREngine:
    @staticmethod
    def extract_text(file_path):
        try:
            image =Image.open(file_path) #open images
            text = pytesseract.image_to_string(image) # extract image from images
            return text
        except Exception as e:
            return str(e)