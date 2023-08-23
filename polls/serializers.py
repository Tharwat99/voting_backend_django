from rest_framework import serializers
from .models import Poll, Choice

class ChoiceSerializer(serializers.ModelSerializer):
    """
    Choice serializer to serializer choice data. 
    """
    voting_count = serializers.SerializerMethodField()
    class Meta:
        model = Choice
        fields = ['id', 'choice_text', 'voting_count']
    def get_voting_count(self, obj):
        return obj.vote_set.filter(confirmed= True).count()

class ListPollSerializer(serializers.ModelSerializer):
    """
    List polls serializer to serializer polls data.
    """
    choices = ChoiceSerializer(many=True)
    class Meta:
        model = Poll
        fields = ['id', 'title', 'description', 'expiry_date', 'is_expired', 'choices']