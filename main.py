import uvicorn
from fastapi import FastAPI, Request
from contextlib import asynccontextmanager

from starlette.responses import JSONResponse

from graph import get_graph_builder
from app.schema.email_schema import EmailRequest

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.graph = get_graph_builder()
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/email/")
async def generate_customer_email(email: EmailRequest, request: Request):
    try:
        graph = request.app.state.graph
        config = {"configurable": {"thread_id":email.thread_id}}
        result = await graph.ainvoke({"raw_input": email.input}, config)
        return result
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
