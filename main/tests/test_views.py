from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Article, Category, Comment

class ArticleDetailViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name='Test Category', slug='test-category')
        self.article = Article.objects.create(
            title='Test Article',
            content='This is a test article.',
            author=self.user,
            slug='test-article',
            meta_description='Test meta description.'
        )
        self.article.categories.add(self.category)

    def test_article_detail_view(self):
        url = reverse('article_detail', kwargs={'slug': self.article.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class CommentFormViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name='Test Category', slug='test-category')
        self.article = Article.objects.create(
            title='Test Article',
            content='This is a test article.',
            author=self.user,
            slug='test-article',
            meta_description='Test meta description.'
        )
        self.article.categories.add(self.category)

    def test_add_comment(self):
        url = reverse('article_detail', kwargs={'slug': self.article.slug})
        response = self.client.post(url, {'author': 'Test User', 'email': 'test@example.com', 'content': 'Test comment'})
        self.assertEqual(response.status_code, 302)  # Check for redirection after successful comment submission
