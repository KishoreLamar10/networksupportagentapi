import os
import json
from fastapi import FastAPI, Request as FastAPIRequest
from pydantic import BaseModel
from typing import List, Optional
from app.graph.support_graph import support_graph
from app.agents.retrieval_agent import retriever
from app.agents.support_agent import support_node_stream
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, StreamingResponse

# --- Rate Limiting ---
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

limiter = Limiter(key_func=get_remote_address, default_limits=["60/minute"])

app = FastAPI(
    title="NetSupport AI API",
    description="AI-powered multi-agent network troubleshooting assistant using RAG.",
    version="2.0.0",
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, lambda req, exc: __import__("fastapi.responses", fromlist=["JSONResponse"]).JSONResponse(
    status_code=429,
    content={"detail": "Rate limit exceeded. Please try again later."},
))
app.add_middleware(SlowAPIMiddleware)

# --- CORS ---
ALLOWED_ORIGINS = os.getenv(
    "ALLOWED_ORIGINS",
    "http://localhost:3000,http://localhost:3737,https://genai-support-ui.vercel.app,https://networksupportagent.vercel.app"
).split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- Models ---
class HistoryMessage(BaseModel):
    role: str
    content: str

class SupportRequest(BaseModel):
    query: str
    history: Optional[List[HistoryMessage]] = []

class SourceDoc(BaseModel):
    source: str
    preview: str

class SupportResponse(BaseModel):
    answer: str
    sources: List[SourceDoc]


# --- Endpoints ---

@app.get("/health")
def health_check():
    return {"status": "ok", "model": os.getenv("MODEL_NAME", "gpt-4.1-nano")}


@app.post("/support", response_model=SupportResponse)
@limiter.limit("20/minute")
def support(req: SupportRequest, request: FastAPIRequest):
    history = [{"role": m.role, "content": m.content} for m in (req.history or [])]
    result = support_graph.invoke({
        "query": req.query,
        "retrieved_docs": [],
        "answer": "",
        "history": history,
    })
    docs = result["retrieved_docs"]
    sources = [
        SourceDoc(source=d.metadata["source"], preview=d.page_content[:150])
        for d in docs
    ]
    return SupportResponse(answer=result["answer"], sources=sources)


@app.post("/support/stream")
@limiter.limit("20/minute")
async def support_stream(req: SupportRequest, request: FastAPIRequest):
    """SSE streaming endpoint — yields tokens as they are generated."""
    history = [{"role": m.role, "content": m.content} for m in (req.history or [])]

    # Retrieve documents first
    docs = retriever.retrieve(req.query)
    sources = [
        {"source": d.metadata["source"], "preview": d.page_content[:150]}
        for d in docs
    ]

    state = {
        "query": req.query,
        "retrieved_docs": docs,
        "answer": "",
        "history": history,
    }

    def event_generator():
        # Send sources first
        yield f"data: {json.dumps({'type': 'sources', 'sources': sources})}\n\n"
        # Stream tokens
        for token in support_node_stream(state):
            yield f"data: {json.dumps({'type': 'token', 'token': token})}\n\n"
        # Signal completion
        yield f"data: {json.dumps({'type': 'done'})}\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>NetSupport AI API</title>
            <style>
                body {
                    font-family: 'Segoe UI', system-ui, sans-serif;
                    padding: 40px;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    min-height: 100vh;
                    margin: 0;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                }
                .card {
                    background: white;
                    padding: 40px;
                    border-radius: 20px;
                    max-width: 600px;
                    box-shadow: 0 20px 60px rgba(0,0,0,0.2);
                }
                h1 { color: #1e40af; margin-top: 0; }
                a {
                    color: #4f46e5;
                    font-weight: 600;
                    text-decoration: none;
                }
                a:hover { text-decoration: underline; }
                code {
                    background: #f1f5f9;
                    padding: 2px 8px;
                    border-radius: 6px;
                    font-size: 14px;
                }
                .endpoints { margin-top: 20px; }
                .endpoint {
                    background: #f8fafc;
                    padding: 12px 16px;
                    border-radius: 10px;
                    margin: 8px 0;
                    border-left: 4px solid #4f46e5;
                }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>⚡ NetSupport AI API</h1>
                <p>Intelligent, multi-agent, RAG-powered network support assistant.</p>
                <p>📘 <a href="/docs">Swagger API Docs</a></p>
                <div class="endpoints">
                    <div class="endpoint"><code>POST /support</code> — Get support response</div>
                    <div class="endpoint"><code>POST /support/stream</code> — Stream response (SSE)</div>
                    <div class="endpoint"><code>GET /health</code> — Health check</div>
                </div>
            </div>
        </body>
    </html>
    """
