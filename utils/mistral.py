# utils/mistral_summary.py

from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import os

# Load from environment variable or set directly
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

client = MistralClient(api_key=MISTRAL_API_KEY)
model = "mistral-medium"  # or "mistral-7b-instruct" if self-hosted

def get_mistral_summary(summary_text: str) -> str:
    """
    Generate a plain-language summary of a policy using Mistral 7B.
    """
    messages = [
        ChatMessage(role="system", content="You are a helpful policy assistant. Summarize U.S. legislation in plain, concise English for the average citizen."),
        ChatMessage(role="user", content=f"Summarize this policy:\n{summary_text}")
    ]

    response = client.chat(model=model, messages=messages)
    return response.choices[0].message.content.strip()
