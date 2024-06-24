from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Category, Article, Comment, Profile

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category', slug='test-category')

    def test_category_creation(self):
        self.assertEqual(self.category.name, 'Test Category')
        self.assertEqual(self.category.slug, 'test-category')

class ArticleModelTest(TestCase):
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

    def test_article_creation(self):
        self.assertEqual(self.article.title, 'Test Article')
        self.assertEqual(self.article.content, 'This is a test article.')
        self.assertEqual(self.article.author.username, 'testuser')
        self.assertEqual(self.article.slug, 'test-article')
        self.assertEqual(self.article.meta_description, 'Test meta description.')
        self.assertIn(self.category, self.article.categories.all())

class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.article = Article.objects.create(
            title='Test Article',
            content='This is a test article.',
            author=self.user,
            slug='test-article',
            meta_description='Test meta description.'
        )
        self.comment = Comment.objects.create(
            article=self.article,
            author='Test Commenter',
            email='test@example.com',
            content='This is a test comment.'
        )

    def test_comment_creation(self):
        self.assertEqual(self.comment.article.title, 'Test Article')
        self.assertEqual(self.comment.author, 'Test Commenter')
        self.assertEqual(self.comment.email, 'test@example.com')
        self.assertEqual(self.comment.content, 'This is a test comment.')

class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        if not Profile.objects.filter(user=self.user).exists():
            self.profile = Profile.objects.create(user=self.user, image='profile_pics/default.jpg')

    def test_profile_creation(self):
        profile = Profile.objects.get(user=self.user)
        self.assertEqual(profile.user.username, 'testuser')
        self.assertEqual(str(profile.image), 'profile_pics/default.jpg')


# main/tests/test_models.py for the chatbot logic
from django.test import TestCase
from ..models import ChatbotInteraction

class ChatbotInteractionModelTest(TestCase):
    def setUp(self):
        self.interaction = ChatbotInteraction.objects.create(
            user_question='What is the weather today?',
            chatbot_response='The weather is sunny.'
        )

    def test_chatbot_interaction_creation(self):
        self.assertEqual(self.interaction.user_question, 'What is the weather today?')
        self.assertEqual(self.interaction.chatbot_response, 'The weather is sunny.')

# main/tests/test_models.py

from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Category, Article, Comment, Profile, ChatbotInteraction

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category', slug='test-category')

    def test_category_creation(self):
        self.assertEqual(self.category.name, 'Test Category')
        self.assertEqual(self.category.slug, 'test-category')

class ArticleModelTest(TestCase):
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

    def test_article_creation(self):
        self.assertEqual(self.article.title, 'Test Article')
        self.assertEqual(self.article.content, 'This is a test article.')
        self.assertEqual(self.article.author.username, 'testuser')
        self.assertEqual(self.article.slug, 'test-article')
        self.assertEqual(self.article.meta_description, 'Test meta description.')
        self.assertIn(self.category, self.article.categories.all())

class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.article = Article.objects.create(
            title='Test Article',
            content='This is a test article.',
            author=self.user,
            slug='test-article',
            meta_description='Test meta description.'
        )
        self.comment = Comment.objects.create(
            article=self.article,
            author='Test Commenter',
            email='test@example.com',
            content='This is a test comment.'
        )

    def test_comment_creation(self):
        self.assertEqual(self.comment.article.title, 'Test Article')
        self.assertEqual(self.comment.author, 'Test Commenter')
        self.assertEqual(self.comment.email, 'test@example.com')
        self.assertEqual(self.comment.content, 'This is a test comment.')

class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile.objects.create(user=self.user, image='profile_pics/default.jpg')

    def test_profile_creation(self):
        self.assertEqual(self.profile.user.username, 'testuser')
        self.assertEqual(str(self.profile.image), 'profile_pics/default.jpg')

class ChatbotInteractionModelTest(TestCase):
    def setUp(self):
        self.interaction = ChatbotInteraction.objects.create(
            user_question='Hello, chatbot!',
            chatbot_response='Hello, user!'
        )

    def test_chatbot_interaction_creation(self):
        self.assertEqual(self.interaction.user_question, 'Hello, chatbot!')
        self.assertEqual(self.interaction.chatbot_response, 'Hello, user!')
