from fastapi import FastAPI
from app.routes import chat

app = FastAPI(
    title="Easy Chatbot",
    description="Chatbot contextual para documentos usando Ollama + LangChain",
    version="0.1.0"
)

app.include_router(chat.router)
