from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from app.graph.support_graph import support_graph
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
