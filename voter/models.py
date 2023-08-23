from django.db import models
from django.utils import timezone
import pyotp
from polls.models import Poll, Choice
from .utils import send_otp_mail

class Voter(models.Model):
    """
    Voter Model.
    """
    email = models.EmailField(unique=True)
    polls_voted = models.ManyToManyField(Poll, through='Vote')

    def __str__(self):
        return str(self.email)

class Vote(models.Model):
    """
    Vote Model.
    """
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
    otp_valid_until = models.DateTimeField(null=True, blank=True)
    confirmed = models.BooleanField(default=False)

    
    def generate_otp(self, valid_duration_minutes):
        """
        method to generate otp and set otp_validate_until.
        """
        secret_key= pyotp.random_base32()
        totp = pyotp.TOTP(secret_key, digits=6)
        self.otp = totp.now()
        self.otp_valid_until = timezone.now() + timezone.timedelta(seconds=valid_duration_minutes*60)
        self.save()
        send_otp_mail(self.otp, self.voter.email)
        return self.otp
    
    def verify_otp_expired(self):
        """
        method to verfiy otp if expired or not.
        """
        if timezone.now() > self.otp_valid_until:
            return True
        else:
            return False
    def verify_otp_correct(self, token):
        """
        method to verfiy otp if correct or not
        """
        if str(self.otp) != token:
            return True
        else:
            return False
    class Meta:
        unique_together = ['voter', 'poll']