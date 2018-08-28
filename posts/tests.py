from django.test import TestCase
from .models import Post


class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text='Mock text')

    def test_post_content(self):
        post = Post.objects.get(id=1)
        self.assertEqual(f'{post.text}', 'Mock text')