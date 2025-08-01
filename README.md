# 🧠 Easy ChatBot

Un microservicio API que permite crear un chatbot contextualizado a partir de documentos cargados por el usuario (PDF, DOCX, TXT). Utiliza modelos LLM locales (via Ollama) para responder consultas, generar resúmenes y simular conversaciones útiles para el estudio o el onboarding empresarial.

### 🚀 Tecnologías principales

- 🧠 [LangChain](https://python.langchain.com/)
- 🔀 [LangGraph](https://github.com/langchain-ai/langgraph)
- 🤖 LLM local vía [Ollama](https://ollama.com/) (`mistral`, `llama3`, etc.)
- 📦 [Poetry](https://python-poetry.org/) para gestión de dependencias
- ⚡ [FastAPI](https://fastapi.tiangolo.com/) como servidor REST
- 🧭 [FAISS](https://github.com/facebookresearch/faiss) o ChromaDB como motor vectorial

### 🧩 Funcionalidad actual

- `POST /upload`: cargar documentos (PDF, TXT, DOCX)
- `POST /chat`: hacer preguntas sobre los documentos cargados
- Memoria conversacional y recuperación de contexto (RAG)
- Soporte multicliente (por `user_id`)

### 🌱 Roadmap

- [ ] Integración con AWS Bedrock
- [ ] Mapas conceptuales (visualización)
- [ ] Plugin CLI o interfaz web
- [ ] Publicar como imagen Docker lista para probar
- [ ] Soporte para múltiples contextos por organización/persona

### 🔧 Requisitos

- Python 3.10+
- Ollama corriendo en segundo plano
- `poetry install` para instalar dependencias


### Uso

Instalar dependencias y levantar entorno virtual
```
poetry install
poetry env activate
```

Correr servidor
```bash
uvicorn app.main:app --reload --port 8000
```

Pruebas en Postman o bash
```bash
curl -X POST http://localhost:8000/upload \
  -F "file=@/ruta/a/documento.pdf" \
  -F "user_id=test_user"

curl -X POST http://localhost:8000/chat \
  -F "message=¿De qué trata el documento?" \
  -F "user_id=test_user"
```

### 🐳 Docker (TODO)

```bash
docker build -t easy_chatbot .
docker run -p 8000:8000 easy_chatbot
```