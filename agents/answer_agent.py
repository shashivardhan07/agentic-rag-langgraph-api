from langchain_core.messages import HumanMessage, AIMessage
from llm_client import llm

def generate_answer(state):
    docs = state["retrieved_docs"]
    context = "\n\n".join(d.page_content for d in docs)

    prompt = f"""
    Use ONLY the context to answer:
    
    Context:
    {context}

    Question: {state['query']}
    """

    answer = llm.invoke([HumanMessage(content=prompt)])
    state["messages"].append(AIMessage(content=answer.content))

    return state
