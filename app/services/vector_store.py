from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from app.config import VECTOR_DB_PATH
from app.config import OLLAMA_MODEL

def save_documents(documents, user_id: str):
    embeddings = OllamaEmbeddings(model=OLLAMA_MODEL)
    db_path = f"{VECTOR_DB_PATH}_{user_id}"
    vectorstore = FAISS.from_documents(documents, embedding=embeddings)
    vectorstore.save_local(db_path)

def get_retriever(user_id: str):
    db_path = f"{VECTOR_DB_PATH}_{user_id}"
    embeddings = OllamaEmbeddings()
    vectorstore = FAISS.load_local(db_path, embeddings)
    return vectorstore.as_retriever()
