from langchain_community.document_loaders import PyPDFLoader, TextLoader, UnstructuredWordDocumentLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import tempfile
import os

def load_and_split(filename: str, content: bytes, user_id: str):
    ext = os.path.splitext(filename)[1].lower()

    with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
        tmp.write(content)
        tmp_path = tmp.name

    if ext == ".pdf":
        loader = PyPDFLoader(tmp_path)
    elif ext == ".txt":
        loader = TextLoader(tmp_path)
    elif ext == ".docx":
        loader = UnstructuredWordDocumentLoader(tmp_path)
    else:
        raise ValueError("Formato no soportado")

    documents = loader.load()
    for doc in documents:
        doc.metadata["user_id"] = user_id

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.split_documents(documents)
