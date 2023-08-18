from django.db import models
from django.utils import timezone

class Poll(models.Model):
    """
    Poll Model.
    """
    title = models.CharField(max_length=150)
    description = models.TextField()
    expiry_date = models.DateTimeField()

    def is_expired(self):
        return self.expiry_date < timezone.now()
    
    def __str__(self):
        return str(self.title)

class Choice(models.Model):
    """
    Choice Model.
    """
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=150)
    
    def __str__(self):
        return str(self.choice_text)

