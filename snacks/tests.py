from django.test import SimpleTestCase
from django.urls import reverse
class TestingPages(SimpleTestCase):
    def test_home_response(self):
        # reverse 
        url = reverse("home")
        response =self.client.get(url)
        self.assertEqual(response.status_code,200)
