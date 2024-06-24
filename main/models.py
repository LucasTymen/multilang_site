# main/models.py

from django.db import models
from django.contrib.auth.models import User

# Model for article categories
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

# Model for articles
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateField(auto_now_add=True)  # Automatically set the publication date
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name='articles')
    slug = models.SlugField(unique=True)
    meta_description = models.TextField()

    def __str__(self):
        return self.title

# Model for comments on articles
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    publication_date = models.DateField(auto_now_add=True)  # Automatically set the publication date

    def __str__(self):
        return f'Comment by {self.author} on {self.article}'

# Model for user profiles
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

# Model for chatbot interactions
class ChatbotInteraction(models.Model):
    user_question = models.TextField()
    chatbot_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_question
