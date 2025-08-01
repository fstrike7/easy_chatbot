from langchain_community.chat_models import ChatOllama
from langchain.chains import RetrievalQA
from app.config import OLLAMA_MODEL

def get_chat_response(message: str, retriever):
    llm = ChatOllama(model=OLLAMA_MODEL)
    chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    result = chain.run(message)
    return result.strip()
