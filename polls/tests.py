from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

class AttendanceListCreateViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_polls_list_pages_view(self):
        url = reverse('list-polls-pages')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # TODO Add assertions to check the response data