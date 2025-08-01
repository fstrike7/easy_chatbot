import os
import uuid
from pathlib import Path
from typing import Union
from fastapi import UploadFile, HTTPException

import fitz  # PyMuPDF para PDFs
from docx import Document  # para DOCX

ALLOWED_EXTENSIONS = {".pdf", ".docx", ".txt"}
MAX_FILE_SIZE_MB = 8
UPLOAD_DIR = Path("storage/uploads")

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

def is_allowed_file(filename: str) -> bool:
    return Path(filename).suffix.lower() in ALLOWED_EXTENSIONS

def sanitize_filename(filename: str) -> str:
    ext = Path(filename).suffix
    name = Path(filename).stem
    return f"{name[:50]}_{uuid.uuid4().hex}{ext}"

def validate_file(file: UploadFile):
    ext = Path(file.filename).suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail=f"Archivo no permitido: {ext}")
    size_mb = len(file.file.read()) / (1024 * 1024)
    file.file.seek(0)
    if size_mb > MAX_FILE_SIZE_MB:
        raise HTTPException(status_code=400, detail=f"Archivo demasiado grande (> {MAX_FILE_SIZE_MB}MB)")

def convert_to_text(file_path: Path) -> str:
    ext = file_path.suffix.lower()
    if ext == ".pdf":
        text = ""
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()
        return text
    elif ext == ".docx":
        doc = Document(file_path)
        return "\n".join([p.text for p in doc.paragraphs])
    elif ext == ".txt":
        return file_path.read_text(encoding="utf-8")
    else:
        raise ValueError("Tipo de archivo no soportado para extracción de texto")

def save_and_process_file(file: UploadFile) -> dict:
    validate_file(file)
    filename = sanitize_filename(file.filename)
    saved_path = UPLOAD_DIR / filename

    with open(saved_path, "wb") as f:
        f.write(file.file.read())

    text_content = convert_to_text(saved_path)

    return {
        "filename": filename,
        "text": text_content,
        "path": str(saved_path),
    }