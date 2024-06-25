import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Make a test API call
try:
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Hello, how can I assist you?",
        max_tokens=50,
    )
    print("API call successful. Response:")
    print(response.choices[0].text.strip())
except openai.OpenAIError as e:
    print(f"OpenAI API error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
