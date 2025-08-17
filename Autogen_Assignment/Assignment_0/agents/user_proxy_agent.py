from autogen_agentchat.agents import UserProxyAgent

def getInnerUserProxyAgent():
    inner_user_proxy_agent = UserProxyAgent(
        name="InnerUserProxyAgent",
        input_func = input,
        Description = "Human-in-the-loop who supervises the inner team's analysis," \
        "providing feedback or approval."
    )
    return inner_user_proxy_agent