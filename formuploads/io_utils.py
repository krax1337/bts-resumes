import os
from .pdf_utils import pdf_to_text
from .docx_utils import docx_to_text

def read_pdf_and_docx(dir_path):
    txt = None
    f = dir_path
    if f.lower().endswith('.docx') or f.lower().endswith('doc'):
        txt = docx_to_text(f)
    elif f.lower().endswith('.pdf'):
        txt = pdf_to_text(f)
    return txt