from langchain_core.messages import HumanMessage
from llm_client import llm

def rewrite_query(state):
    prompt = f"Rewrite this query for better search: {state['query']}"
    new_query = llm.invoke([HumanMessage(content=prompt)]).content.strip()

    state["query"] = new_query
    state["retry_count"] += 1

    return state
