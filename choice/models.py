from django.db import models
from polls.models import Poll

class Choice(models.Model):
    """
    Choice Model.
    """
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=150)

