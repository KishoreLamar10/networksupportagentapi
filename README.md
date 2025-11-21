🛠️ GenAI Multi-Agent Support Backend
FastAPI • LangGraph • LangChain • FAISS • Retrieval-Augmented Generation (RAG)
This backend powers an AI-driven technical support assistant using a multi-agent architecture and a RAG pipeline. It retrieves relevant troubleshooting documents and generates intelligent, context-aware solutions.
🚀 Features
🔹 Multi-Agent System
Retrieval Agent — fetches relevant documents from FAISS vector store
Support Agent — synthesizes human-like troubleshooting responses
Powered by LangGraph for deterministic multi-step reasoning
🔹 RAG (Retrieval-Augmented Generation)
Embeddings generated using OpenAI Embeddings API
Stored inside a FAISS vector database
Searches across support articles, router troubleshooting guides, and more
🔹 FastAPI Web Service
Exposes a simple API endpoint:
POST /support
Input:
{ "query": "my router internet light is off" }
Output:
{
"answer": "Please restart your router and check the WAN cable...",
"sources": []
}
🔹 Cloud Deployment
Fully deployed on Render
Automatic FAISS indexing during deployment (render.yaml)
📁 Project Structure
app/
┣ agents/
┃ ┣ retrieval_agent.py
┃ ┗ support_agent.py
┣ rag/
┃ ┣ index_builder.py
┃ ┗ retriever.py
┣ graph/
┃ ┗ support_graph.py
┣ api/
┃ ┗ server.py
┗ data/
┣ docs/ # troubleshooting files
┗ faiss_index/ # auto-generated FAISS index

main.py
render.yaml
requirements.txt
🔑 Environment Variables
Create .env:
OPENAI_API_KEY=<your key>
MODEL_NAME=gpt-4o-mini
DOCS_PATH=app/data/docs
🏗️ How to Run Locally
Install dependencies
pip install -r requirements.txt
Build vector index
python3 -m app.rag.index_builder
Run the server
uvicorn app.api.server:app --reload
Open Swagger docs:
👉 http://127.0.0.1:8000/docs
☁️ Deployment (Render)
This project includes a render.yaml that:
Installs requirements
Builds FAISS index
Starts FastAPI server
Backend URL:
👉 https://genai-multi-agent-support.onrender.com
📦 Technologies Used
FastAPI
LangChain / LangGraph
FAISS Vector Store
OpenAI Embeddings
Python 3.11
Render Cloud Deployment
