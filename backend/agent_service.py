import os
import httpx
from dotenv import load_dotenv

load_dotenv()

MCP_SERVER_URL = os.getenv("MCP_SERVER_URL")


async def send_generated_email(to: str, subject: str, body: str):
    payload = {
        "to": to,
        "subject": subject,
        "body": body
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(MCP_SERVER_URL, json=payload)
        response.raise_for_status()

    return {
        "status": "success",
        "to": to,
        "subject": subject,
        "body": body,
        "mcp_response": response.json()
    }



'''import os
import requests
from dotenv import load_dotenv

load_dotenv()

MCP_SERVER_URL = os.getenv("MCP_SERVER_URL")


def send_generated_email(to: str, subject: str, body: str):
    payload = {
        "to": to,
        "subject": subject,
        "body": body
    }

    response = requests.post(MCP_SERVER_URL, json=payload)

    return {
        "status": "success",
        "to": to,
        "subject": subject,
        "body": body,
        "mcp_response": response.json()
    }
    '''