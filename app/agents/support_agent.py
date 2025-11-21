from typing import List, TypedDict
from langchain_openai import ChatOpenAI
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from app.config import settings

class SupportState(TypedDict):
    query: str
    retrieved_docs: List[Document]
    answer: str

llm = ChatOpenAI(
    api_key=settings.OPENAI_API_KEY,
    model=settings.MODEL_NAME,
    temperature=0.2,
)

SYSTEM_PROMPT = """You are a support assistant.
Use ONLY the provided documents.
Be clear, step-by-step."""

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("human", "Question: {query}\n\nDocuments:\n{context}")
])

def format_docs(docs: List[Document]) -> str:
    return "\n\n".join(
        f"[DOC {i}] {d.metadata['source']}\n{d.page_content}"
        for i, d in enumerate(docs)
    )

def support_node(state: SupportState):
    context = format_docs(state["retrieved_docs"])
    response = (prompt | llm).invoke({"query": state["query"], "context": context})
    return {
        "query": state["query"],
        "retrieved_docs": state["retrieved_docs"],
        "answer": response.content,
    }
