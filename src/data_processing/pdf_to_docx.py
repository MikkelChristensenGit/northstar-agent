from pdf2docx import Converter

def pdf_to_docx(pdf_path, docx_path):
    """Convert a pdf to docx"""
    cv = Converter(pdf_path)
    cv.convert(docx_path)
    cv.close()
