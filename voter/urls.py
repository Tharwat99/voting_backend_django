from django.urls import path
from . views import CreateVoteAPIView, ValidateOTPVoteAPIView
urlpatterns = [
    path('create-vote/', CreateVoteAPIView.as_view(), name = "create-vote"),
    path('validate-vote-otp/<int:id>/', ValidateOTPVoteAPIView.as_view(), name = "validate-vote-otp")
]