import os
from dotenv import load_dotenv

from autogen_core.models import ModelFamily
from autogen_ext.models.openai import OpenAIChatCompletionClient
from config.constant import OPENAI_MODEL, OPENAI_BASE_URL

load_dotenv()
#api_key = os.getenv("OPENAI_API_KEY")
#api_key = os.getenv("GOOGLE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    #raise ValueError("OPENAI_API_KEY is not set in environment variable")
    raise ValueError("GROQ_API_KEY is not set in environment variable")

def get_model_client():
    model_client = OpenAIChatCompletionClient(
        model=OPENAI_MODEL,
        base_url=OPENAI_BASE_URL,
        api_key=GROQ_API_KEY,
        model_info = {
            "vision": False,
            "function_calling": True,
            "json_output": True,
            "family": ModelFamily.UNKNOWN,
            "structured_output": True,
        }
    )
    return model_client