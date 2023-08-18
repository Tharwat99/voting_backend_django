from rest_framework import serializers
from .models import Poll, Choice

class ChoiceSerializer(serializers.ModelSerializer):
    """
    Choice serializer to serializer choice data. 
    """
    class Meta:
        model = Choice
        fields = ['id', 'choice_text']

class ListPollSerializer(serializers.ModelSerializer):
    """
    List polls serializer to serializer polls data.
    """
    choices = ChoiceSerializer(many=True)
    class Meta:
        model = Poll
        fields = ['id', 'title', 'description', 'expiry_date', 'is_expired', 'choices']