import os
import re
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)


def clean_text(text):
    if not text:
        return "No response."

    # Remove markdown
    text = text.replace("**", "")
    text = text.replace("###", "")
    text = text.replace("##", "")
    text = text.replace("```", "")

    # Remove multiple blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Remove extra spaces
    text = re.sub(r"[ \t]+", " ", text)

    return text.strip()


def ask_gemini(prompt):

    response = client.chat.completions.create(
        model="deepseek/deepseek-r1-0528",
        messages=[
            {
                "role": "system",
                "content": """
You are DocMind AI.

Always reply in clean readable English.

Rules:
- Never use Markdown.
- Never use ** or ##.
- Use headings.
- Use bullet points.
- Use numbering when explaining.
- Keep answers well formatted.
- Leave blank lines between sections.
"""
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=1200,
    )

    answer = response.choices[0].message.content

    return clean_text(answer)