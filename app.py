from flask import Flask, render_template, request, redirect, url_for
from ocr_engine import OCREngine
from utils.utils import allowed_file, save_uploaded_file
