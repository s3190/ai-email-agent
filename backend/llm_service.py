import os
import re
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_email(context: str):
    prompt = f"""
You are an expert assistant that writes clear, professional, and context-aware emails.

Task:
Generate a professional email based on the provided context.

Context:
{context}

Instructions:
- Understand the intent of the context before writing
- Generate a concise, relevant, and meaningful subject line
- Write a well-structured email with:
  - A proper greeting
  - A clear purpose in the first paragraph
  - Supporting details if needed
  - A polite closing
- Maintain a professional, polite, and natural tone
- Keep the email concise and avoid unnecessary repetition
- Do NOT use placeholders like [Your Name], [Recipient], etc.
- Always sign the email as "Susmitha"
- Adapt the tone based on context

IMPORTANT:
- Output ONLY in the exact format below
- Do NOT add explanations
- Do NOT add markdown
- Do NOT add extra text before or after

Subject: <clear subject line>
Body:
<email body>
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You write clear, polite, professional emails and strictly follow output formats."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
    )

    content = response.choices[0].message.content.strip()

    print("LLM OUTPUT:\n", content)

    subject_match = re.search(r"Subject:\s*(.+)", content)
    body_match = re.search(r"Body:\s*([\s\S]+)", content)

    if subject_match:
        subject = subject_match.group(1).strip()
    else:
        subject = "No Subject"

    if body_match:
        body = body_match.group(1).strip()
    else:
        body = content

    return subject, body