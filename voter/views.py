from rest_framework import generics, permissions
from . models import Vote
from .serializers import CreateVoteSerializer, UpdateVoteSerializer

class CreateVoteAPIView(generics.CreateAPIView):
    serializer_class = CreateVoteSerializer
    queryset = Vote.objects.all()
    permission_classes = [permissions.AllowAny]

class ValidateOTPVoteAPIView(generics.UpdateAPIView):
    serializer_class = UpdateVoteSerializer
    queryset = Vote.objects.all()
    permission_classes = [permissions.AllowAny]
    lookup_field = "id"
