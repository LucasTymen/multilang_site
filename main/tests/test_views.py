from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Category, Article, Comment

class ArticleListViewTest(TestCase):
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

    def test_article_list_view(self):
        response = self.client.get(reverse('article_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Article')

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
        response = self.client.get(reverse('article_detail', kwargs={'slug': self.article.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Article')
        self.assertContains(response, 'This is a test article.')

class CommentFormViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.article = Article.objects.create(
            title='Test Article',
            content='This is a test article.',
            author=self.user,
            slug='test-article',
            meta_description='Test meta description.'
        )

    def test_add_comment(self):
        response = self.client.post(reverse('article_detail', kwargs={'slug': self.article.slug}), {
            'author': 'Test Commenter',
            'email': 'test@example.com',
            'content': 'This is a test comment.'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Commenter')
        self.assertContains(response, 'This is a test comment.')
