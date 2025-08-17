from autogen_agentchat.agents import AssistantAgent

def getFlightSearchAgent(model_client):
    flight_search_agent = AssistantAgent(
    name="FlightSearchAgent",
    model_client=model_client,
    system_message="You are FlightAgent, specialized in finding and recommending flight options based on user preferences such " \
    "as destination, travel dates, preferred airlines, and budget. Provide clear, concise flight options including airline names, " \
    "flight times, prices, and any important booking details."
    )
    return flight_search_agent
