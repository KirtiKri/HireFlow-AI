from io import BytesIO
from docx import Document
from pypdf import PdfReader

MAX_BYTES = 5 * 1024 * 1024

def extract_text(filename: str, contents: bytes) -> str:
    if not contents or len(contents) > MAX_BYTES:
        raise ValueError("File must be non-empty and no larger than 5 MB")
    suffix = filename.lower().rsplit(".", 1)[-1]
    if suffix == "txt":
        text = contents.decode("utf-8")
    elif suffix == "pdf":
        reader = PdfReader(BytesIO(contents))
        if len(reader.pages) > 15:
            raise ValueError("PDF must be 15 pages or fewer")
        text = "\n".join(page.extract_text() or "" for page in reader.pages)
    elif suffix == "docx":
        doc = Document(BytesIO(contents))
        text = "\n".join(p.text for p in doc.paragraphs)
    else:
        raise ValueError("Supported formats: PDF, DOCX, TXT")
    if not text.strip():
        raise ValueError("No extractable text found. Scanned documents need OCR, which is not enabled.")
    return text[:50000]
