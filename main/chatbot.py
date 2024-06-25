# main/chatbot.py

import openai
from django.conf import settings

def get_chatbot_response(user_question):
    """
    Function to get response from OpenAI's GPT-3 model.
    """
    openai.api_key = settings.OPENAI_API_KEY
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_question,
        max_tokens=150
    )
    response_text = response.choices[0].text.strip()
    return response_text
