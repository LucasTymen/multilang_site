from django.test import TestCase
from ..forms import CommentForm

class CommentFormTest(TestCase):
    def test_comment_form_valid_data(self):
        form = CommentForm(data={
            'author': 'Test Commenter',
            'email': 'test@example.com',
            'content': 'This is a test comment.'
        })
        self.assertTrue(form.is_valid())

    def test_comment_form_invalid_data(self):
        form = CommentForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)  # Adjust the number according to your form's required fields
        self.assertIn('content', form.errors)  # Make sure to include actual missing field in your form


# testing the chatbot response logic
from django.test import TestCase
from ..forms import ChatbotInteractionForm

class ChatbotInteractionFormTest(TestCase):
    def test_chatbot_interaction_form_valid_data(self):
        form = ChatbotInteractionForm(data={
            'user_question': 'What is the weather today?',
            'chatbot_response': 'The weather is sunny.'
        })
        self.assertTrue(form.is_valid())

    def test_chatbot_interaction_form_invalid_data(self):
        form = ChatbotInteractionForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)  # Adjusted based on required fields

# main/tests/test_forms.py

from django.test import TestCase
from ..forms import CommentForm

class CommentFormTest(TestCase):
    def test_comment_form_valid_data(self):
        form = CommentForm(data={
            'content': 'This is a test comment.'
        })
        self.assertTrue(form.is_valid())

    def test_comment_form_invalid_data(self):
        form = CommentForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)  # Only 'content' field is required
