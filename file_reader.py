from PyPDF2 import PdfReader
from docx import Document

def read_pdf(file):

    reader=PdfReader(file)

    text=""

    for page in reader.pages:
        text+=page.extract_text()

    return text

def read_docx(file):

    doc=Document(file)

    text=""

    for p in doc.paragraphs:
        text+=p.text

    return text

def read_txt(file):

    with open(file,"r",encoding="utf8") as f:
        return f.read()