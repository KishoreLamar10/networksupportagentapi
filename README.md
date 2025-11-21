# 🛠️ GenAI Multi-Agent Support Backend

### FastAPI • LangGraph • LangChain • FAISS • RAG

This backend powers an AI-driven **technical support assistant** using a multi-agent architecture and a Retrieval-Augmented Generation (RAG) pipeline.  
It retrieves relevant troubleshooting content and generates intelligent, step-by-step resolutions.

---

## 🚀 Features

### 🔹 Multi-Agent Architecture

- **Retrieval Agent** — Retrieves relevant documents using FAISS
- **Support Agent** — Produces human-like troubleshooting responses
- Agents orchestrated using **LangGraph** workflow execution

### 🔹 RAG (Retrieval-Augmented Generation)

- Embeddings generated with OpenAI Embeddings API
- Vector search using **FAISS**
- Supports Markdown-based troubleshooting files
- Deterministic document retrieval structure

### 🔹 FastAPI Web Server

Main endpoint:

**POST `/support`**

Example request:

```json
{ "query": "my router internet light is off" }
```

Example response:

```json
{
  "answer": "Restart your router, check cables, verify WAN connection...",
  "sources": []
}
```

### 🔹 Cloud Deployment (Render)

Deployed URL:

👉 https://genai-multi-agent-support.onrender.com

Automated steps:

- Install dependencies
- Build FAISS index
- Start FastAPI server

---

## 📁 Project Structure

```
app/
  agents/
    retrieval_agent.py
    support_agent.py
  rag/
    index_builder.py
    retriever.py
  graph/
    support_graph.py
  api/
    server.py
  data/
    docs/
    faiss_index/
main.py
render.yaml
requirements.txt
```

---

## 🔧 Environment Variables

Create **.env**:

```
OPENAI_API_KEY=your-key
MODEL_NAME=gpt-4o-mini
DOCS_PATH=app/data/docs
```

---

## 🏗️ Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Build the FAISS index:

```bash
python3 -m app.rag.index_builder
```

Start the server:

```bash
uvicorn app.api.server:app --reload
```

Open Swagger docs:

👉 http://127.0.0.1:8000/docs

---

## 🧰 Technologies

- FastAPI
- LangChain
- LangGraph
- FAISS
- OpenAI Embeddings
- Python 3.11
- Render Deployment

---
