from rest_framework import generics, permissions
from . models import Vote
from .serializers import CreateVoteSerializer

class CreateVoteAPIView(generics.CreateAPIView):
    serializer_class = CreateVoteSerializer
    queryset = Vote.objects.all()
    permission_classes = [permissions.AllowAny]
