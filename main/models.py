from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# the categories of the articles
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

# The articles
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    slug = models.SlugField(unique=True)
    meta_description = models.TextField()

    def __str__(self):
        return self.title

# The comments
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    publication_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.article}'

# Configuring User profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
