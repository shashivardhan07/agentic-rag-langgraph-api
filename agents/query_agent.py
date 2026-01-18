from langchain_core.messages import HumanMessage, AIMessage
from llm_client import llm

def generate_query_or_respond(state):
    user_message = state["messages"][-1].content

    needs_retrieval = any(
        w in user_message.lower()
        for w in ["what", "who", "when", "where", "how", "rag", "langgraph"]
    )

    if not needs_retrieval:
        resp = llm.invoke([HumanMessage(content=user_message)])
        state["messages"].append(AIMessage(content=resp.content))
    else:
        state["query"] = user_message

    return state
