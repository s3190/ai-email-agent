from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from llm_service import generate_email
from agent_service import send_generated_email

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PreviewEmailRequest(BaseModel):
    to: str
    context: str


class SendEmailRequest(BaseModel):
    to: str
    subject: str
    body: str


@app.get("/")
def home():
    return {"message": "AI Email Agent Backend Running"}


@app.post("/agent/preview-email")
def preview_email(req: PreviewEmailRequest):
    try:
        subject, body = generate_email(req.context)
        return {
            "to": req.to,
            "subject": subject,
            "body": body
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/agent/confirm-send")
async def confirm_send(req: SendEmailRequest):
    try:
        return await send_generated_email(req.to, req.subject, req.body)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))