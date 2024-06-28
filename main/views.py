# main/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import Article, Comment, ChatbotInteraction
from .forms import ArticleForm, CommentForm, UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ChatbotInteractionForm
from .chatbot import get_chatbot_response
import openai
import os
from openai import OpenAI
from django.conf import settings
from django.http import JsonResponse
import json

# Home page view
def home(request):
    articles = Article.objects.all()
    return render(request, 'main/home.html', {'articles': articles})

# List articles
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'main/article_list.html', {'articles': articles})

# Detailed view of an article
def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    comments = article.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('article_detail', slug=slug)
    else:
        form = CommentForm()
    return render(request, 'main/article_detail.html', {'article': article, 'comments': comments, 'form': form})

# Create an article
@login_required
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            form.save_m2m()
            return redirect('article_detail', slug=article.slug)
    else:
        form = ArticleForm()
    return render(request, 'main/article_form.html', {'form': form})

# Update an article
@login_required
def article_update(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.user != article.author:
        return redirect('article_detail', slug=slug)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', slug=article.slug)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'main/article_form.html', {'form': form})

# Delete an article
@login_required
def article_delete(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.user == article.author:
        article.delete()
        return redirect('article_list')
    return redirect('article_detail', slug=slug)

# Register a user
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('article_list')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form})

# Define the profile view
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'main/profile.html', {'u_form': u_form, 'p_form': p_form})

# Delete an account
@login_required
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('article_list')
    return render(request, 'main/delete_account.html')

# Chatbot view
def chatbot(request):
    if request.method == "POST":
        answer_text = "An error occurred. Please try again later."
        user_message = json.loads(request.body).get("message")
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        try:
            answer = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
                    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
                ]
            )
            answer_text = answer.choices[0].text.strip()
        except openai.APIConnectionError as e:
            print("The server could not be reached")
            print(e.__cause__)  # an underlying Exception, likely raised within httpx.
        except openai.RateLimitError as e:
            print("A 429 status code was received; we should back off a bit.")
        except openai.APIStatusError as e:
            print("Another non-200-range status code was received")
            print(e.status_code)
            print(e.response)
        # Save the interaction in the database
        # interaction = ChatbotInteraction(user_question=user_message, chatbot_response=answer_text)
        # interaction.save()
        return JsonResponse({"answer": answer_text})
    return render(request, "main/chatbot.html")
