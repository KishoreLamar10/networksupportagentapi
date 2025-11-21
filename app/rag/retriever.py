from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from app.config import settings

INDEX_PATH = "app/data/faiss_index"

class RAGRetriever:
    def __init__(self, k=4):
        self.embeddings = OpenAIEmbeddings(api_key=settings.OPENAI_API_KEY)
        self.vectorstore = FAISS.load_local(
            INDEX_PATH,
            self.embeddings,
            allow_dangerous_deserialization=True
        )
        self.retriever = self.vectorstore.as_retriever(search_kwargs={"k": k})

    def retrieve(self, query: str):
        # Updated for LangChain 0.2+
        return self.retriever.invoke(query)
