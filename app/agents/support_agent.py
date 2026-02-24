from typing import List, TypedDict
from langchain_openai import ChatOpenAI
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from app.config import settings

class SupportState(TypedDict):
    query: str
    retrieved_docs: List[Document]
    answer: str
    history: List[dict]

llm = ChatOpenAI(
    api_key=settings.OPENAI_API_KEY,
    model=settings.MODEL_NAME,
    temperature=0.2,
)

SYSTEM_PROMPT = """You are NetSupport AI, an expert network troubleshooting assistant.
Use ONLY the provided documents to answer the user's question.
If the documents don't contain relevant information, say so honestly.
Be clear, concise, and provide step-by-step instructions when applicable.
Use markdown formatting for better readability (bold, lists, code blocks).
If the user is following up on a previous message, use the conversation history for context."""

prompt_with_history = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("human", "Conversation History:\n{history}\n\nQuestion: {query}\n\nRelevant Documents:\n{context}")
])

prompt_no_history = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("human", "Question: {query}\n\nRelevant Documents:\n{context}")
])

def format_docs(docs: List[Document]) -> str:
    return "\n\n".join(
        f"[DOC {i}] {d.metadata['source']}\n{d.page_content}"
        for i, d in enumerate(docs)
    )

def format_history(history: List[dict]) -> str:
    if not history:
        return ""
    lines = []
    for msg in history[-6:]:  # Keep last 6 messages for context
        role = msg.get("role", "user")
        content = msg.get("content", "")
        lines.append(f"{role.upper()}: {content}")
    return "\n".join(lines)

def support_node(state: SupportState):
    context = format_docs(state["retrieved_docs"])
    history = state.get("history", [])

    if history:
        history_str = format_history(history)
        response = (prompt_with_history | llm).invoke({
            "query": state["query"],
            "context": context,
            "history": history_str,
        })
    else:
        response = (prompt_no_history | llm).invoke({
            "query": state["query"],
            "context": context,
        })

    return {
        "query": state["query"],
        "retrieved_docs": state["retrieved_docs"],
        "answer": response.content,
        "history": history,
    }

def support_node_stream(state: SupportState):
    """Generator that yields tokens for SSE streaming."""
    context = format_docs(state["retrieved_docs"])
    history = state.get("history", [])

    if history:
        history_str = format_history(history)
        chain = prompt_with_history | llm
        invoke_args = {"query": state["query"], "context": context, "history": history_str}
    else:
        chain = prompt_no_history | llm
        invoke_args = {"query": state["query"], "context": context}

    for chunk in chain.stream(invoke_args):
        if chunk.content:
            yield chunk.content
