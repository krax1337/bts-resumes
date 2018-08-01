import os
from .pdf_utils import pdf_to_text
from .docx_utils import docx_to_text
from .doc_utils import doc_to_text
from .rtf_utils import rtf_to_text

def read_pdf_and_docx(dir_path):
    txt = None
    f = dir_path
    if f.lower().endswith('.docx'):
        txt = docx_to_text(f)
    elif f.lower().endswith('.pdf'):
        txt = pdf_to_text(f)
    elif f.lower().endswith('.doc'):
        txt = doc_to_text(f)
    elif f.lower().endswith('.rtf'):
        txt = rtf_to_text(f)
    print(txt)    
    return txt
