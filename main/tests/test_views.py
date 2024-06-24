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



# main/tests/test_views.py for the chatbot response logic

from django.test import TestCase
from django.urls import reverse
from ..models import ChatbotInteraction

class ChatbotViewTest(TestCase):
    def test_chatbot_view_get(self):
        response = self.client.get(reverse('chatbot_view'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Chatbot')

    def test_chatbot_view_post(self):
        response = self.client.post(reverse('chatbot_view'), {
            'user_question': 'What is the weather today?',
        })
        self.assertEqual(response.status_code, 302)  # Assuming a redirect after form submission
        interaction = ChatbotInteraction.objects.last()
        self.assertEqual(interaction.user_question, 'What is the weather today?')
        self.assertTrue(interaction.chatbot_response)  # Ensure a response was generated


# main/tests/test_views.py

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Article, Comment, Category

class ArticleDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
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
        response = self.client.get(reverse('article_detail', args=[self.article.slug]))
        self.assertEqual(response.status_code, 200)

class CommentFormViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.article = Article.objects.create(
            title='Test Article',
            content='This is a test article.',
            author=self.user,
            slug='test-article',
            meta_description='Test meta description.'
        )

    def test_add_comment(self):
        response = self.client.post(reverse('article_detail', args=[self.article.slug]), {
            'content': 'This is a test comment.'
        })
        self.assertEqual(response.status_code, 302)  # Check for redirection after successful comment submission
