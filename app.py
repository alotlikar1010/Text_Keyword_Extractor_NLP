from flask import Flask, render_template, request, redirect, url_for
from ocr_engine import OCREngine
from utils.utils import allowed_file, save_uploaded_file
from pdf_extract import extract_text_pdf
import os

app =Flask(__name__)

app.config['UPLOAD_FOLDER']= 'uploads'

# if upload dir does not exist code
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


app.route('/',methods =['GET','POST'])
def index():
    if request.method =='POST':
        file = request.files['file']

        file_type = request.form['file-type'] # image or pdf

        if file and allowed_file(file.filename):
            filename = save_uploaded_file(file)
            if filename:
                file_path = os.path.join(app.config['UPLOAD_FOLDER'],filename)
                extracted_text =""

                if file_type == 'image':
                    ocr= OCREngine()
                    extracted_text = ocr.extract_text(file_path)
                elif file_type == 'pdf':
                    extracted_text = extract_text_pdf(file_path)

                return render_template('index.html',extracted_text=extracted_text)
        
    return render_template('index.html',extracted_text=None)

if __name__ == '__main__':
    app.run(debug=True)