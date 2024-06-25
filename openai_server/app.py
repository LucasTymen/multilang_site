# openai_server/app.py
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
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message},
            ]
        )
        response_text = response['choices'][0]['message']['content'].strip()
        return jsonify({"response": response_text})
    except openai.error.InvalidRequestError as e:
        return jsonify({"error": str(e)}), 400
    except openai.error.OpenAIError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8003)
