from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/chatbot', methods=['POST'])
def chatbot():
    try:
        user_message = request.json.get("message")
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=user_message,
            max_tokens=150,
        )
        response_text = response.choices[0].text.strip()
        return jsonify({"response": response_text})
    except openai.error.OpenAIError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
