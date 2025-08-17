from autogen_agentchat.agents import AssistantAgent

def getHotelSearchAgent(model_client):
    hotel_search_agent = AssistantAgent(
        name="HotelSSearchAgent",
        model_client=model_client,
        system_message="You are the HotelAgent specialized in finding suitable hotel options based on user preferences and " \
        "constraints. Provide a list of hotels matching the destination, budget, dates, and other user requirements. " \
        "Prioritize well-reviewed hotels and clearly mention key features such as price, location, and amenities."
    )
    return hotel_search_agent