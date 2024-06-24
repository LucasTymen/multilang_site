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
        self.assertEqual(len(form.errors), 3)  # Expecting errors for all required fields
