from app.graph.support_graph import support_graph

while True:
    q = input("You: ")
    if q.lower() in ["exit", "quit"]:
        break
    result = support_graph.invoke({"query": q, "retrieved_docs": [], "answer": ""})
    print("Assistant:", result["answer"])
