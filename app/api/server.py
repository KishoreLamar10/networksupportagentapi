from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from app.graph.support_graph import support_graph
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # TEMPORARY - allow all during development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Request(BaseModel):
    query: str

class SourceDoc(BaseModel):
    source: str
    preview: str

class Response(BaseModel):
    answer: str
    sources: List[SourceDoc]

@app.post("/support", response_model=Response)
def support(req: Request):
    result = support_graph.invoke({"query": req.query, "retrieved_docs": [], "answer": ""})
    docs = result["retrieved_docs"]
    sources = [
        SourceDoc(source=d.metadata["source"], preview=d.page_content[:150])
        for d in docs
    ]
    return Response(answer=result["answer"], sources=sources)

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>GenAI Support API</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    padding: 40px;
                    background: #f8fafc;
                }
                h1 {
                    color: #1e40af;
                }
                .card {
                    background: white;
                    padding: 20px;
                    border-radius: 12px;
                    max-width: 600px;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                }
                a {
                    color: #1e3a8a;
                    font-weight: bold;
                }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>GenAI Multi-Agent Support API</h1>
                <p>Welcome! This API powers an intelligent, multi-agent, retrieval-augmented technical support assistant.</p>
                <p>📘 To view documentation and test endpoints, visit:</p>
                <p><a href="/docs">Swagger API Docs</a></p>
                <p>🚀 Main endpoint:</p>
                <pre>POST /support</pre>
            </div>
        </body>
    </html>
    """
