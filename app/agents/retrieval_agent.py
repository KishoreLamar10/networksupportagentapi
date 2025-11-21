from typing import List, TypedDict
from langchain_core.documents import Document
from app.rag.retriever import RAGRetriever

class RetrievalState(TypedDict):
    query: str
    retrieved_docs: List[Document]

retriever = RAGRetriever(k=4)

def retrieval_node(state: RetrievalState) -> RetrievalState:
    docs = retriever.retrieve(state["query"])
    return {"query": state["query"], "retrieved_docs": docs}
