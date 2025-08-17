import os
from autogen_ext.models.openai import OpenAIChatCompletionClient
from config.constants import MODEL_OPENAI
from config.config import OPENAI_API_KEY
from dotenv import load_dotenv

load_dotenv()

def get_model_client():
    openai_model_client = OpenAIChatCompletionClient(
        model=MODEL_OPENAI,
        api_key=OPENAI_API_KEY
    )
    return openai_model_client