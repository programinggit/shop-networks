from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class HelloWorldViewTestCase(APITestCase):
    def test_hello_world_view(self):
        url = reverse('hello_world')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'message': 'Hello, World!'})
