import openai
from django.conf import settings

def get_chatbot_response(message):
    openai.api_key = settings.OPENAI_API_KEY
    response = openai.Completion.create(
        engine="davinci",
        prompt=message,
        max_tokens=150
    )
    return response.choices[0].text.strip()
