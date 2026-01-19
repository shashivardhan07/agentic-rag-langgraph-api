# 🤖 Agentic RAG API using LangGraph, LangChain & FastAPI

An **Agentic Retrieval-Augmented Generation (RAG)** system built using **LangGraph** and **LangChain**, exposed as an **API** using **FastAPI / Flask**.  
This project demonstrates how multiple LLM-powered agents can **collaborate, reason, retrieve, evaluate, and generate answers** in a structured graph-based workflow.

---

## 🚀 Features

- Agentic RAG architecture using LangGraph
- Modular LLM agents with clear responsibilities
- Dynamic query rewriting and routing
- Document retrieval using vector databases
- Answer generation with evaluation and grading
- API-based interface (FastAPI / Flask)
- Clean, production-ready project structure

---

## 🧠 Agentic Workflow

The system uses **multiple agents**, each responsible for a specific task:

1. **Query Agent** – understands or reformulates user queries  
2. **Retrieval Agent** – fetches relevant documents from the vector store  
3. **Grader Agent** – evaluates retrieved documents for relevance  
4. **Rewrite Agent** – improves the query if retrieval quality is low  
5. **Answer Agent** – generates the final answer using the LLM  
6. **Graph Builder** – orchestrates the agents using LangGraph  

This loop continues until a high-quality answer is produced.

---

## 📂 Project Structure

<pre>
agentic-rag-langgraph-api/
├── app.py                  # API entry point (Flask / FastAPI)
├── graph_builder.py        # LangGraph workflow definition
├── llm_client.py           # LLM configuration and client
├── vectorstore.py          # Vector database setup
├── requirements.txt
├── README.md
│
├── agents/
│   ├── __init__.py
│   ├── query_agent.py
│   ├── retrieval_agent.py
│   ├── grader_agent.py
│   ├── rewrite_agent.py
│   └── answer_agent.py
</pre>

---

## 🛠️ Tech Stack

- Python
- LangChain
- LangGraph
- FastAPI / Flask
- Vector Databases (FAISS / Pinecone)
- Large Language Models (Gemini / OpenAI / Groq)
- dotenv for environment management

---

## ⚙️ Environment Setup

Create a `.env` file using the template below:

LLM_API_KEY=your_llm_api_key

VECTOR_DB_API_KEY=your_vector_db_key

