from django.test import TestCase

# Create your tests here.
from rest_framework.test import APIClient

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_data(self):
        response = self.client.post('/data/', {'10 Min Std dev': 10, 'Time': 1.76, 'DateTime': '5/01/2022 12:20:00', '10 Min Sampled Avg': 22.9}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['Date'], '05-January-2022')

    # Add more tests for GET, PUT, DELETE
