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