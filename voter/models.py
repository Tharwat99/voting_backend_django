from django.db import models
from polls.models import Poll, Choice

class Voter(models.Model):

    email = models.EmailField(unique=True)
    polls_voted = models.ManyToManyField(Poll, through='Vote')
    def __str__(self):
        return str(self.id)

class Vote(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)