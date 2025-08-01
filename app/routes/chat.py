from fastapi import APIRouter, UploadFile, File, Form
from app.services.document_loader import load_and_split
from app.services.vector_store import save_documents, get_retriever
from app.services.chatbot import get_chat_response

router = APIRouter()

@router.post("/upload")
async def upload_document(file: UploadFile = File(...), user_id: str = Form(...)):
    contents = await file.read()
    docs = load_and_split(file.filename, contents, user_id)
    save_documents(docs, user_id)
    return {"status": "ok", "chunks": len(docs)}

@router.post("/chat")
def chat(user_id: str = Form(...), message: str = Form(...)):
    retriever = get_retriever(user_id)
    response = get_chat_response(message, retriever)
    return {"response": response}
