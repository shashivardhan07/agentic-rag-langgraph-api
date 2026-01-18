from langgraph.graph import StateGraph
from langgraph.constants import START, END

from typing import TypedDict, List
from langchain_core.messages import HumanMessage

# Import agents
from agents.query_agent import generate_query_or_respond
from agents.retrieval_agent import retrieve_documents
from agents.grader_agent import grade_documents, route_from_grader
from agents.rewrite_agent import rewrite_query
from agents.answer_agent import generate_answer


class AgentState(TypedDict):
    messages: List
    query: str
    retrieved_docs: list
    retry_count: int


def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("generate_query_or_respond", generate_query_or_respond)
    graph.add_node("retrieve_documents", retrieve_documents)
    graph.add_node("grade_documents", grade_documents)
    graph.add_node("rewrite_query", rewrite_query)
    graph.add_node("generate_answer", generate_answer)

    graph.add_edge(START, "generate_query_or_respond")
    graph.add_edge("generate_query_or_respond", "retrieve_documents")
    graph.add_edge("retrieve_documents", "grade_documents")

    graph.add_conditional_edges(
        "grade_documents",
        route_from_grader,
        {
            "generate_answer": "generate_answer",
            "rewrite_query": "rewrite_query"
        }
    )

    graph.add_edge("rewrite_query", "retrieve_documents")
    graph.add_edge("generate_answer", END)

    return graph.compile()


graph = build_graph()


def run_rag_pipeline(query: str):
    initial_state = {
        "messages": [HumanMessage(content=query)],
        "query": "",
        "retrieved_docs": [],
        "retry_count": 0
    }
    result = graph.invoke(initial_state)
    return result["messages"][-1].content
