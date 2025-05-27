# Import necessary libraries
# This module contains the ProductInfo class, which is used to store and manage product information.
import os
import gradio as gr
from dotenv import load_dotenv
from typing import List
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Define the ProductInfo class
class ProductInfo(BaseModel):
    """
    ProductInfo class to store and manage product information.
    """
    product_name: str = Field(description="Name of the product")
    product_description: List[str] = Field(description="Description of the product")
    product_price: int = Field(description="Price of the product")
    
# Define the LLM model for product information extraction
llm = ChatGroq(
    model = "gemma2-9b-it",
    temperature = 0.1,
)

# Define the output parser for JSON format
json_parser = JsonOutputParser(pydantic_object=ProductInfo)

# Define the prompt template for extracting product information
prompt_template = ChatPromptTemplate(
    messages=[
        ("system", "You are a helpful product assistant that provides detailed information about products in JSON format. For any query provide product name, product description and product price in USD."),
        ("user", "{query}"),
        ("assistant", "Here is the product information in required format: {format_instructions}")
    ],
    input_variables=["query"],
    partial_variables={"format_instructions": json_parser.get_format_instructions()}
)


# Create chain for extracting product information
chain = prompt_template | llm | json_parser

try:
    # invoke the chain with a sample text
    response = chain .invoke({"query": "Tell me about Samsung Galaxy S25 Ultra"})
    # Print the response
    print(response)
except Exception as e:
    # Print the error message if any exception occurs
    print(f"An error occurred: {e}")