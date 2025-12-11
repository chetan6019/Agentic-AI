import email
from langchain_core.prompts import PromptTemplate

from app.config.app_config import SOURCE_TYPE_EMAIL, SOURCE_TYPE_MESSAGE, templates, LLM
from app.state.agentState import AgentState

def parse_input(state: AgentState) -> AgentState:
    """Parse raw input date to check if input is email or just a plain message."""

    raw = state['raw_input']

    # Check whether the raw input is an email
    if 'Subject' in raw and 'From' in raw:
        msg = email.message_from_string(raw)
        state['subject'] = msg['Subject']
        state['body'] = msg.get_payload()
        state['source_type'] = SOURCE_TYPE_EMAIL
    else:
        state['subject'] = 'Customer Complaint'
        state['body'] = raw
        state['source_type'] = SOURCE_TYPE_MESSAGE

    return state

def classify_intent(state: AgentState) -> AgentState:
    """Classify the query type."""
    intent  = state['body'].lower()
    if "refund" in intent:
        state['category'] = "Refund Request"
    elif "late" in intent or "delay" in intent or "not arrived" in intent:
        state['category'] = "Delivery Issue"
    else:
        state['category'] = "General Inquiry"

    return state

# def select_template(state: AgentState) -> AgentState:
#     """Select template based on query category"""

#     category = state['category']
#     if category == "Refund Request":
#         state['template'] = templates['refund_request']
#     elif category == "Delivery Issue":
#         state['template'] = templates['delivery_issue']
#     else:
#         state['template'] = templates['generic']

#     return state
def select_template(state: AgentState) -> AgentState:
    """Set prompt based on category"""

    category = state['category']

    prompts = """
    You are a customer service representative who is resolving customer related issues.
    Analyze the customer queries or issues and write a professional email based on the customer queries. 
    Categorize the queries into different issues as given in the below example: 
    1. Refund Request
    2. Delivery issue
    3. General Inquiry
    Customer Complaint: {complaint}
    Your response should contain the below format
    ```Hi [Customer Name],
       Email body
       signature
    ```
    """
    state['prompt_template'] = prompts
    return state

def generate_email(state: AgentState) -> AgentState:
    """Generate email response using LLM and selected template."""

    # final_template = """
    #     Customer Complaint: {complaint}
    #     Use this template 
    #     Template: {template}
    #     Write a professional reply email.  
    #     """
    
    # prompt = PromptTemplate(
    #     template=final_template
    # )
    prompt = PromptTemplate(
        template=state['prompt_template'],
        input_variables=["complaint"]
    )

    chain = prompt | LLM
    
    response = chain.invoke({'complaint': state['body']})

    #state['draft_response'] = response.content
    state['final_response'] = response.content

    return state
