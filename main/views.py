# main/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group
from .models import Article, Comment, ChatbotInteraction
from .forms import ArticleForm, CommentForm, UserRegisterForm, UserUpdateForm, ProfileUpdateForm
import openai
import os
from django.http import JsonResponse
import json

# Function to check if user belongs to a specific group
def group_required(group_name):
    def in_group(u):
        if u.is_authenticated:
            if bool(u.groups.filter(name=group_name)) | u.is_superuser:
                return True
        return False
    return user_passes_test(in_group)

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
@group_required('Administrateur')
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

            # Add user to "Visiteur" group
            group = Group.objects.get(name='Visiteur')
            user.groups.add(group)

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
        user_message = json.loads(request.body).get("message")
        client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        answer_text = "An error occurred. Please try again later."
        try:
            answer = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
                    {"role": "user", "content": user_message}
                ]
            )
            answer_text = answer.choices[0].message['content'].strip()
        except openai.error.OpenAIError as e:
            answer_text = str(e)
        # Save the interaction in the database
        interaction = ChatbotInteraction(user_question=user_message, chatbot_response=answer_text)
        interaction.save()
        return JsonResponse({"answer": answer_text})
    return render(request, "main/chatbot.html")

# Search view
def search(request):
    if 'q' in request.GET:
        query = request.GET['q']
        articles = Article.objects.filter(title__icontains(query))
    else:
        articles = Article.objects.all()
    return render(request, 'main/search.html', {'articles': articles})

# Documentation view
def documentation(request):
    return redirect('http://localhost:8001')
