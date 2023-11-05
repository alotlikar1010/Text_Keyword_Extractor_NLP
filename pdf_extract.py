import fitz


def extract_text_pdf(pdf_path):
    try:
        pdf_doc = fitz.open(pdf_path)
        text =""

        for page_num in range(pdf_doc.page_count):
            page = pdf_doc[page_num]
            text += page.get_text()
        return text
    except Exception as e:
        return str(e)