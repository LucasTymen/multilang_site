# main/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Article, Comment, Profile, ChatbotInteraction

# Form for user registration
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Form for updating user information
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

# Form for updating user profile
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

# Form for creating and updating articles
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'categories', 'slug', 'meta_description']

# Form for adding comments to articles
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

# Form for chatbot interactions
class ChatbotInteractionForm(forms.ModelForm):
    class Meta:
        model = ChatbotInteraction
        fields = ['user_question', 'chatbot_response']
