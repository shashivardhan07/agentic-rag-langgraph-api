from vectorstore import retriever

def retrieve_documents(state):
    docs = retriever.get_relevant_documents(state["query"])
    state["retrieved_docs"] = docs
    return state
