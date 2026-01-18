from langchain_core.messages import HumanMessage
from llm_client import llm

def grade_documents(state):
    return state  # LangGraph only needs state updated

def route_from_grader(state):
    docs = state["retrieved_docs"]
    query = state["query"]

    prompt = f"""
    Query: {query}
    Docs: {[d.page_content for d in docs]}
    Are these docs enough? yes or no.
    """

    result = llm.invoke([HumanMessage(content=prompt)])

    return "generate_answer" if "yes" in result.content.lower() else "rewrite_query"
