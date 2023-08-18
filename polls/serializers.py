from rest_framework import serializers
from .models import Poll, Choice

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'choice_text']

class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)
    class Meta:
        model = Poll
        fields = ['id', 'title', 'description', 'expiry_date', 'choices']