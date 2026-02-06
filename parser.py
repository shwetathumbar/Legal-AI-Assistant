import pdfplumber
from docx import Document


def parse_document(uploaded_file):
    """
    Extract text from uploaded contract files.
    Supports PDF, DOCX, and TXT.
    Works correctly with Streamlit uploads.
    """

    filename = uploaded_file.name.lower()

    if filename.endswith(".pdf"):
        return _read_pdf(uploaded_file)

    elif filename.endswith(".docx"):
        return _read_docx(uploaded_file)

    elif filename.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")

    else:
        raise ValueError("Unsupported file format")


def _read_pdf(uploaded_file):
    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text


def _read_docx(uploaded_file):
    doc = Document(uploaded_file)
    return "\n".join(p.text for p in doc.paragraphs if p.text)
