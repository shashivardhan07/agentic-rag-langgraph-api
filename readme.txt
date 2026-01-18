project/
│── app.py                <-- Flask app
│── agents/
│     ├── query_agent.py
│     ├── retrieval_agent.py
│     ├── grader_agent.py
│     ├── rewrite_agent.py
│     ├── answer_agent.py
│── graph_builder.py      <-- Combine all agents into LangGraph
│── vectorstore.py        <-- Embeddings + FAISS
│── llm_client.py         <-- Groq LLM initialization
