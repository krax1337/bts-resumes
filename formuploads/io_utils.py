import os

from .doc_utils import doc_to_text
from .docx_utils import docx_to_text
from .pdf_utils import pdf_to_text
from .rtf_utils import rtf_to_text


def read_pdf_and_docx(dir_path):
    txt = None
    f = dir_path
    print(dir_path)
    if f.lower().endswith('.docx'):
        txt = docx_to_text(f)
    elif f.lower().endswith('.pdf'):
        txt = pdf_to_text(f)
    elif f.lower().endswith('.doc'):
        txt = doc_to_text(f)
    elif f.lower().endswith('.rtf'):
        txt = rtf_to_text(f)
    if len(txt) <= 1:
        f1 = f[:-4]
        print(f1)
        os.rename(f , f1 + ".rtf")
        txt = rtf_to_text(f1 + ".rtf")
    print(txt)
    return txt
