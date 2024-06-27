# openai_server/urls.py
from django.urls import path
from .views import chatbot_ask, chatbot_response

urlpatterns = [
    path('chatbot_ask/', chatbot_ask, name='chatbot_ask'),
    path('chatbot_response/', chatbot_response, name='chatbot_response'),
]
