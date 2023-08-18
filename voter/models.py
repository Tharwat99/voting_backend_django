from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from . manager import VoterManager
from polls.models import Poll

class Voter(AbstractUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    polls_voted = models.ManyToManyField(Poll, through='Vote')
    username = None
    first_name = None
    last_name = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = VoterManager()

    def __str__(self):
        return str(self.id)