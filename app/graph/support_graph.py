from typing import List, TypedDict
from langchain_core.documents import Document
from langgraph.graph import StateGraph, END
from app.agents.retrieval_agent import retrieval_node
from app.agents.support_agent import support_node

class GraphState(TypedDict):
    query: str
    retrieved_docs: List[Document]
    answer: str

def build_graph():
    workflow = StateGraph(GraphState)

    workflow.add_node("retrieval", retrieval_node)
    workflow.add_node("support", support_node)

    workflow.set_entry_point("retrieval")
    workflow.add_edge("retrieval", "support")
    workflow.add_edge("support", END)

    return workflow.compile()

support_graph = build_graph()
