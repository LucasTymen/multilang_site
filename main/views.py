from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import Article, Comment, Category
from .forms import ArticleForm, CommentForm, UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.utils.translation import gettext as _

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
            form.save()
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
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
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
