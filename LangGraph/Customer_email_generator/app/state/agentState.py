from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage

class AgentState(TypedDict):
    raw_input: str      # original query or message from the customer
    source_type: str    # indicates whether the message is from an email or a plain text message.
    subject: str        # The subject of the message, usually extracted from the customer’s query (e.g., "Refund Request").
    body: str           # The main content of the customer’s message or inquiry.
    category: str       # The type of issue or request, such as a "refund," "technical support," or "account query."
    #template: str       # A predefined template for generating responses, which helps in standardizing replies.
    prompt_template: str         # Prompts will be used to generate the responses.
    #draft_response: str # A response that the agent or system is still working on, not yet finalized
    final_response: str # The finalized, polished response that will be sent to the customer.
    message: Annotated[list[BaseMessage], add_messages] # A list of messages (such as conversation history), annotated with add_messages, which could be used to track the ongoing dialogue.
