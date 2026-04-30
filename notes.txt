ai-email-mcp-agent/
│
├── frontend/
│   └── React UI
│
├── backend/
│   ├── main.py
│   ├── agent_service.py
│   ├── llm_service.py
|   |__.env -- contains LLM API key
│   └── requirements.txt
│
├── mcp-server/
│   ├── server.py
│   ├── email_service.py
│   ├── config.py
│   ├── .env ---Contains Gmail credentials
│   └── requirements.txt
│
└── README.md

(.venv) susmithachowdary@Mac backend % uvicorn main:app --reload --port 8000
susmithachowdary@Mac frontend % npm run dev
(.venv) susmithachowdary@Mac mcp-server % uvicorn server:app --reload --port 8001

User enters destination email + context in UI
↓
Frontend sends request to Backend
↓
Backend sends context to Groq LLM
↓
Groq generates subject + email body
↓
Backend calls MCP server tool
↓
MCP server uses Gmail SMTP
↓
Email is sent to destination Gmail

--------------------------------------------------------------------------------------------
What each part does

Frontend React UI

You enter:

{
  "to": "destination@gmail.com",
  "context": "Ask politely about onboarding update"
}

It sends this to:

POST http://127.0.0.1:8000/agent/send-email

Backend FastAPI

The backend receives the request.

Then it calls:

generate_email(context)

This uses Groq LLM to create:

Subject: Follow-up on Onboarding Update

Body:
Hi,
I hope you are doing well...
Best regards,
Susmitha

Agent service

After email is generated, backend prepares payload:

{
  "to": "destination@gmail.com",
  "subject": "Follow-up on Onboarding Update",
  "body": "Hi, I hope you are doing well..."
}

Then it sends this to MCP server:

POST http://127.0.0.1:8001/send-email

MCP Server

The MCP server exposes the email sending tool.

It receives:

to, subject, body

Then calls:

send_email(to, subject, body)

Email service

This connects to Gmail SMTP:

smtp.gmail.com:465

It logs in using:

EMAIL_ADDRESS=yourgmail@gmail.com
EMAIL_PASSWORD=gmail_app_password

Then sends the email.

How to run the project

You need 3 terminals.

Terminal 1: MCP server

cd ~/Downloads/ai-email-agent/mcp-server
source ../.venv/bin/activate
uvicorn server:app --reload --port 8001

Terminal 2: Backend

cd ~/Downloads/ai-email-agent/backend
source ../.venv/bin/activate
uvicorn main:app --reload --port 8000

Terminal 3: Frontend

cd ~/Downloads/ai-email-agent/frontend
npm run dev

Open:

http://localhost:5173

--------------------------------------------------------------------------------------------------------------------
React App.jsx
↓
POST /agent/preview-email
↓
backend/main.py
↓
backend/llm_service.py
↓
Groq LLM generates subject + body
↓
Preview shown in React
↓
User clicks Confirm Send
↓
POST /agent/confirm-send
↓
backend/main.py
↓
backend/agent_service.py
↓
mcp-server/server.py
↓
mcp-server/email_service.py
↓
Gmail SMTP
↓
Email delivered
----------------------------------------------------------------------------------------------------
Groq LLM = thinks/writes email
MCP server = performs action/send email
React UI = user interaction
FastAPI backend = coordinator

In other words,

Frontend = user input
Backend = agent coordinator
LLM = email writer
MCP Server = tool executor
Gmail SMTP = external service

So tomorrow, if you add:
send_slack_message
schedule_calendar_event
query_database
you add them inside MCP server as tools.
Your agent can reuse them without mixing all tool logic into the main backend.
I upgraded the backend-to-MCP communication to async using FastAPI and httpx, so the system can handle external service calls more efficiently and scale better for multiple requests.

MCP-------->In my project, the MCP server acts as a tool layer. The AI agent does not directly handle Gmail logic. It generates the email using Groq LLM, then calls the MCP server’s email tool. This reduces redundant integration code and makes the system extensible, because more tools like calendar, Slack, or database queries can be added to the MCP server later.

Agent------>An agent is any AI system that can reason about a task and take actions. In my project, the backend acts as an agent that generates email content and invokes MCP tools to perform actions like sending emails. MCP allows multiple agents to reuse the same tool layer without duplicating integration logic.

Gaurdrails------->In my project, guardrails are added at multiple levels. The LLM is restricted to generating only a subject and body in a structured format. The user gets a preview before sending, so the AI cannot send emails blindly. The MCP server handles execution separately, and I can add validation checks for recipient email format, empty content, and unsafe instructions before calling Gmail SMTP.

Skill-------> “Reusable unit of procedural knowledge combining instructions + tools to complete a task” 
In my project, an AI skill is implemented as a reusable pipeline that takes user intent, generates structured email content using an LLM, and executes the task through an MCP-based tool layer.


