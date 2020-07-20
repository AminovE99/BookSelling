import unittest

from django.test import TestCase, Client


# Create your tests here.
class TestBookSelling(unittest.TestCase):
    def setUp(self):
        self.test_client = Client()
    def test_get_authors(self):
        response = self.test_client.post('/api/token/ username=vitor password=123', content_type="application/json")
        self.assertEqual(response.status_code, 200)