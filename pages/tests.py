from django.test import SimpleTestCase


class PagesTests(SimpleTestCase):
    def test_home_status_code(self):
        response = self.client.get('/pages/')
        self.assertEqual(response.status_code, 200)


    def test_about_status_code(self):
        response = self.client.get('/pages/about/')
        self.assertEqual(response.status_code, 200)