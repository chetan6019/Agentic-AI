from pydantic import BaseModel, Field

class EmailRequest(BaseModel):
    input: str = Field(..., description="The input text for generating the email.")
    thread_id: str = '1' 
