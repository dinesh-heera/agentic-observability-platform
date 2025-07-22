from langgraph.graph import StateGraph, END
from mcp_router import route_by_intent
from agents import (
    classify_intent, generate_splunk_query,
    run_splunk_query, do_rca, create_jira_ticket
)

class ObservabilityState:
    def __init__(self, prompt, context={}):
        self.prompt = prompt
        self.context = context

async def run_engine(user_prompt: str):
    sg = StateGraph(ObservabilityState)
    sg.add_node("classify", classify_intent)
    sg.add_node("generate_query", generate_splunk_query)
    sg.add_node("run_query", run_splunk_query)
    sg.add_node("rca", do_rca)
    sg.add_node("create_ticket", create_jira_ticket)

    sg.set_entry_point("classify")
    sg.add_edge("classify", "generate_query")
    sg.add_edge("generate_query", "run_query")
    sg.add_edge("run_query", "rca")
    sg.add_edge("rca", "create_ticket")
    sg.add_edge("create_ticket", END)

    graph = sg.compile()
    final_state = await graph.invoke(ObservabilityState(prompt=user_prompt))
    return final_state.context["final_response"]