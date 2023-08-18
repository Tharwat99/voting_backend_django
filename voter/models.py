from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from . manager import VoterManager
from polls.models import Poll, Choice
class Voter(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    polls_voted = models.ManyToManyField(Poll, through='Vote')
    username = None
    first_name = None
    last_name = None
    user_permissions = None
    groups = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = VoterManager()

    def __str__(self):
        return str(self.id)

class Vote(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)