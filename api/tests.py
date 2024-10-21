from django.test import TestCase

# Create your tests here.
from rest_framework.test import APIClient

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_data(self):
        response = self.client.post('/data/', {'DateTime': '2022-01-01 00:00:00'}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['Date'], '01-January-2022')

    # Add more tests for GET, PUT, DELETE
