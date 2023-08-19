from django.urls import path
from . views import CreateVoteAPIView, ValidateOTPVoteAPIView
urlpatterns = [
    path('create-vote', CreateVoteAPIView.as_view()),
    path('validate-vote-otp/<int:id>', ValidateOTPVoteAPIView.as_view())
]