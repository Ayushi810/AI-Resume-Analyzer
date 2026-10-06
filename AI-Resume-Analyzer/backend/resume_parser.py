from pathlib import Path
from pypdf import PdfReader
from docx import Document

def extract_text(file_path):
    path=Path(file_path); extension=path.suffix.lower()
    if extension==".pdf":
        reader=PdfReader(str(path)); return "\n".join(page.extract_text() or "" for page in reader.pages)
    if extension==".docx":
        document=Document(str(path)); return "\n".join(paragraph.text for paragraph in document.paragraphs)
    raise ValueError("Unsupported file format.")
