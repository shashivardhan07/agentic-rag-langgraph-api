from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import FAISS

embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

texts = [
    "LangGraph is a framework for building agentic workflows.",
    "FAISS is a library for efficient similarity search and clustering.",
    "ChatGroq provides ultra-fast LLM inference using Groq hardware.",
    "RAG stands for Retrieval-Augmented Generation."
]

vectorstore = FAISS.from_texts(texts, embedding=embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
