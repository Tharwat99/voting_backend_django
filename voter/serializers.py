from rest_framework import serializers
from .models import Vote, Voter

class CreateVoteSerializer(serializers.ModelSerializer):
    """
    Create vote serializer to serializer voted data created by user.
    """

    def to_internal_value(self, data):
        voter, created = Voter.objects.get_or_create(email = data['voter'])
        data._mutable = True
        data['voter'] = voter.id
        data._mutable = False
        return super().to_internal_value(data)    
    
    class Meta:
        model = Vote
        fields = ['id', 'voter', 'poll', 'choice']
    
    def create(self, validated_data):
        """
        override create method to generate otp when vote created.
        """
        vote_instance = super().create(validated_data)
        vote_instance.generate_otp(10)
        return vote_instance
    
    
    def validate_poll(self, poll):
        if poll.is_expired():
            raise serializers.ValidationError("Poll expired to vote.")
        return poll

class UpdateVoteSerializer(serializers.ModelSerializer):
    """
    Update vote serializer to serializer voted data update by user
    we use it to update confirmed toggle when set correct otp.
    """
    
    class Meta:
        model = Vote
        fields = ['otp', 'confirmed']
    
    
    def update(self, instance, validated_data):
        """
        override update method to update status if otp not expired.
        """
        validated_data['confirmed'] = True
        return super().update(instance, validated_data)
    
    
    def validate_otp(self, otp):
        if self.instance.verify_otp_expired():
            raise serializers.ValidationError("OTP is expired.")
        elif self.instance.verify_otp_correct(otp):
            raise serializers.ValidationError("OTP is not correct.")
        else:
            return otp

