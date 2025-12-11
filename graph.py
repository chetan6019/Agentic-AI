from langgraph.graph import StateGraph, END
from app.node.graph_nodes import parse_input, classify_intent, select_template, generate_email
from app.state.agentState import AgentState
from IPython.display import display, Image

def get_graph_builder():
    builder = StateGraph(AgentState)

    builder.add_node("Parse Input Node", parse_input)
    builder.add_node("Classify Intent Node", classify_intent)
    builder.add_node("Select Template Node", select_template)
    builder.add_node("Generate Email Node", generate_email)

    builder.add_edge("Parse Input Node", "Classify Intent Node")
    builder.add_edge("Classify Intent Node", "Select Template Node")
    builder.add_edge("Select Template Node", "Generate Email Node")
    builder.add_edge("Generate Email Node", END)

    builder.set_entry_point("Parse Input Node")

    return builder.compile()

    #display(Image(graph.get_graph().draw_mermaid_png()))
