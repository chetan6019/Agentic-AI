from autogen_agentchat.agents import AssistantAgent

def getActivityRecommenderAgent(model_client):
    activity_recommender = AssistantAgent(
        name="ActivityRecommenderAgent",
        model_client=model_client,
        system_message="You are the ActivityAgent responsible for suggesting engaging and relevant activities for a user's trip " \
        "based on their destination, interests, time availability, and budget. Provide a variety of options including sightseeing," \
        " cultural experiences, outdoor adventures, and popular local events."
    )
    return activity_recommender