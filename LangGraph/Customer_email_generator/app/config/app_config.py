import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GRQO_API_KEY = os.getenv("GROQ_API_KEY")
if not GOOGLE_API_KEY or not GRQO_API_KEY:
    raise ValueError("GOOGLE_API_KEY or GROQ_API_KEY is not set in environment variables")

# Define LLM model
# LLM = ChatGoogleGenerativeAI(
#     model = "gemini-2.5-flash",
#     api_key=GOOGLE_API_KEY,
#     max_retries=3,
#     temperature=0.3,
# )
LLM = ChatGroq(
    model = "openai/gpt-oss-20b",
    temperature = 0.3,
    api_key = GRQO_API_KEY
)


# templates = {
#     "refund_request": "Hi {{customer}},\n\nWe're sorry to hear about the issue. A refund has been initiated.\n\nThanks,\nSupport Team",
#     "delivery_issue": "Hi {{customer}},\n\nApologies for the delayed delivery. We're investigating the issue.\n\nThanks,\nSupport Team",
#     "generic": "Hi {{customer}}," \
#         "Thank you for reaching out. We'll get back to you shortly." \
#         "Thanks," \
#         "Support Team"
# }

SOURCE_TYPE_EMAIL = "email"
SOURCE_TYPE_MESSAGE = "message"
