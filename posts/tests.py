from django.test import TestCase
from django.urls import reverse
from .models import Post


class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text='Stubbed text')

    def test_post_content(self):
        post = Post.objects.get(id=1)
        self.assertEqual(f'{post.text}', 'Stubbed text')


class PostsHomePageViewTest(TestCase):

    def setUp(self):
        Post.objects.create(text='Stubbed text')

    def test_WhenGetPosts_Then200(self):
        self.assertEqual(self.client.get('/posts/').status_code, 200)

    def test_WhenURLByReverse_Then200(self):
        self.assertEqual(self.client.get(reverse('home')).status_code, 200)

    def test_WhenURLByReverse_ThenUsePostsHomeTemplate(self):
        self.assertTemplateUsed(
            self.client.get(reverse('home')),
            'posts/home.html'
        )