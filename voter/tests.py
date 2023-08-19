from datetime import timedelta
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APIClient
from . models import Vote, Voter
from polls.models import Poll, Choice

class VoteCreateConfirmOTPTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.poll = Poll.objects.create(title='What is the best programming language to use?', description = 'progmming languages', expiry_date=timezone.now() + timedelta(days=1))
        self.choice = Choice.objects.create(choice_text='Python', poll = self.poll)

    def test_create_vote_view(self):
        url = reverse('create-vote')
        data= {
            'voter':"test@gmail.com",
            'poll':self.poll.id,
            'choice':self.choice.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # TODO Add assertions to check the response data and permissions
    