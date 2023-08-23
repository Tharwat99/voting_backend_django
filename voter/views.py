from rest_framework import generics, permissions
from . models import Vote
from .serializers import CreateVoteSerializer, UpdateVoteSerializer

class CreateVoteAPIView(generics.CreateAPIView):
    """
    Create vote for voter.
    """
    serializer_class = CreateVoteSerializer
    queryset = Vote.objects.all()
    permission_classes = [permissions.AllowAny]

class ValidateOTPVoteAPIView(generics.UpdateAPIView):
    """
    Validate and confirm vote by otp.
    """
    serializer_class = UpdateVoteSerializer
    queryset = Vote.objects.all()
    permission_classes = [permissions.AllowAny]
    lookup_field = "id"
