from fastapi import FastAPI
from pydantic import BaseModel
from email_service import send_email

app = FastAPI()


class EmailRequest(BaseModel):
    to: str
    subject: str
    body: str


@app.get("/")
def home():
    return {"message": "MCP Email Server Running"}


@app.post("/send-email")
def send_email_tool(req: EmailRequest):
    result = send_email(req.to, req.subject, req.body)

    return {
        "status": "success",
        "message": result
    }