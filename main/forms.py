from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Article, Comment, Profile  # Assurez-vous d'importer le modèle Profile

# Creating the necessary forms for registration, creation/updating profile, articles, and comments

class UserRegisterForm(UserCreationForm):
    # Email field for registration form
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    # Email field for updating user profile
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    # Image field for updating profile picture
    class Meta:
        model = Profile
        fields = ['image']

class ArticleForm(forms.ModelForm):
    # Form for creating and updating articles
    class Meta:
        model = Article
        fields = ['title', 'content', 'categories', 'slug', 'meta_description']

class CommentForm(forms.ModelForm):
    # Form for adding comments to articles
    class Meta:
        model = Comment
        fields = ['content']
