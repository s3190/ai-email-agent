📧 AI Email Agent (MCP + LLM + Full Stack)

🚀 Overview

This project is an **AI-powered Email Agent** that generates and sends professional emails from a simple user-provided context.

Instead of manually writing emails, users can provide:
- Recipient email(s)
- A short context (e.g., “ask for onboarding update”)

The system:
1. Generates a structured email using an LLM  
2. Shows a preview for confirmation  
3. Sends the email via Gmail automatically  

---

🧠 Key Concept

This project demonstrates **agent-based AI architecture** by separating:

- **Reasoning (LLM)** → generates email content  
- **Execution (MCP server)** → performs real-world actions  

```text
UI → Backend Agent → LLM → MCP Tool → Gmail → Email Sent
````

---

 ✨ Features

* 📄 Generate professional emails from natural language
* 👀 Preview email before sending
* 📬 Send emails to multiple recipients
* 🔌 Modular MCP-based tool integration
* ⚡ Async backend support for scalability
* 🎯 Structured output for reliable execution

---

 🛠️ Tech Stack

Frontend

* React (Vite)
* Axios

Backend (Agent Layer)

* FastAPI
* Python

LLM

* Groq (LLaMA 3)

MCP Tool Server

* FastAPI (separate service)
* Gmail SMTP integration

---

🧩 Architecture

```text
User (React UI)
↓
FastAPI Backend (Agent)
↓
Groq LLM (Email Generation)
↓
MCP Server (Tool Layer)
↓
Gmail SMTP (Execution)
```

---

🧠 AI Skill Implemented

This project implements a reusable AI skill:

```text
Context → Professional Email → Real-world Delivery
```

It combines:

* Prompt-based reasoning
* Structured output generation
* Tool-based execution via MCP

---

🛡️ Guardrails

* Email preview before sending
* Structured output format (Subject / Body)
* Input validation (recipient & content)
* Separation of reasoning and execution

---

⚙️ Setup Instructions

1. Clone Repository

```bash
git clone https://github.com/your-username/ai-email-agent.git
cd ai-email-agent
```

---

 2. Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

4. Environment Variables

 Backend `.env`

```env
GROQ_API_KEY=your_groq_api_key
MCP_SERVER_URL=http://127.0.0.1:8001/send-email
```

 MCP Server `.env`

```env
EMAIL_ADDRESS=yourgmail@gmail.com
EMAIL_PASSWORD=your_app_password
```

---

5. Run Services

Terminal 1 – MCP Server

```bash
cd mcp-server
uvicorn server:app --reload --port 8001
```

Terminal 2 – Backend

```bash
cd backend
uvicorn main:app --reload --port 8000
```

Terminal 3 – Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## 🌐 Usage

1. Open UI
2. Enter:

   * Recipient email(s)
   * Email context
3. Click **Generate Preview**
4. Review generated email
5. Click **Confirm Send**

---

## 🚀 Future Improvements

* Multi-agent workflow support
* Slack / Calendar integrations
* Authentication system
* Deployment (Render / AWS)
* Logging and retry mechanisms

---

## 💡 Learnings

* Designing AI systems beyond prompt engineering
* Building tool-based agent architectures
* Integrating LLMs with real-world services
* Structuring reliable AI workflows

---

## 🤝 Contributions

Feel free to fork, improve, and contribute!

---

## 📬 Contact

If you have feedback or suggestions, feel free to connect!
https://www.linkedin.com/in/susmithathirumala/
