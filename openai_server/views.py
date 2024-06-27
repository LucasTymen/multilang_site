# openai_server/views.py
import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

@csrf_exempt
def chatbot_ask(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message")
        if user_message:
            try:
                response = openai.Completion.create(
                    engine="davinci-codex",
                    prompt=user_message,
                    max_tokens=150
                )
                response_text = response.choices[0].text.strip()
                return JsonResponse({"response": response_text})
            except Exception as e:
                return JsonResponse({"error": str(e)}, status=500)
        else:
            return JsonResponse({"error": "No message provided"}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def chatbot_response(request):
    # Here we assume the response from OpenAI is already handled
    return JsonResponse({"status": "ready"})
