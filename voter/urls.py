from django.urls import path
from . views import CreateVoteAPIView
urlpatterns = [
    path('create-vote', CreateVoteAPIView.as_view())
]