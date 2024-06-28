# main/chatbot.py

import openai
from django.conf import settings

def get_chatbot_response(user_question):
    """
    Function to get response from OpenAI's GPT-3 model.
    """
    openai.api_key = settings.OPENAI_API_KEY
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
    )

    print(completion.choices[0].message)
