from fastapi import FastAPI
from pydantic import BaseModel
from graph_builder import run_rag_pipeline

app = FastAPI(
    title="LangGraph Multi-Agent RAG API",
    version="1.0.0",
    description="A FastAPI wrapper for a multi-agent LangGraph RAG pipeline."
)

class Query(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "LangGraph RAG FastAPI is running!"}


@app.post("/ask")
def ask(query: Query):
    try:
        answer = run_rag_pipeline(query.question)
        return {"question": query.question, "answer": answer}
    except Exception as e:
        return {"error": str(e)}
