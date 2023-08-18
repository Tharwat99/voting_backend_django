from rest_framework import serializers
from .models import Vote, Voter
from polls.models import Poll

class CreateVoteSerializer(serializers.ModelSerializer):
    """
    Create vote serializer to serializer voted data created by user.
    """

    def to_internal_value(self, data):
        voter, created = Voter.objects.get_or_create(email = data['voter'])
        data['voter'] = voter.id
        return super().to_internal_value(data)    
    
    class Meta:
        model = Vote
        fields = ['id', 'voter', 'poll', 'choice']
    
    def validate_poll(self, poll):
        if poll.is_expired:
            raise serializers.ValidationError("Poll expired to vote.")
        return poll