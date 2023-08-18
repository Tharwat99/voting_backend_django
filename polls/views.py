from rest_framework import generics, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from . models import Poll
from .serializers import ListPollSerializer, CreatePollSerializer
from .paginations import PollsListPagination
from .filters import PollsListFilter

class PollListAPIView(generics.ListAPIView):
    serializer_class = ListPollSerializer
    queryset = Poll.objects.all()
    permission_classes = [permissions.AllowAny]
    pagination_class = PollsListPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = PollsListFilter

class PollListAPIView(generics.CreateAPIView):
    serializer_class = CreatePollSerializer
    queryset = Poll.objects.all()
    permission_classes = [permissions.AllowAny]

# class PollListAPIView(generics.ListAPIView):
#     serializer_class = PollSerializer
#     queryset = Poll.objects.all()

#     # def get_queryset(self):
#     #     queryset = super().get_queryset()
#     #     search_term = self.request.query_params.get('search', None)
#     #     if search_term:
#     #         queryset = queryset.filter(
#     #             models.Q(title__icontains=search_term) |
#     #             models.Q(description__icontains=search_term) |
#     #             models.Q(choices__choice_text__icontains=search_term)
#     #         ).distinct()
#     #     return queryset.order_by('-expiry_date')

#     # def list(self, request, *args, **kwargs):
#     #     queryset = self.get_queryset()
#     #     page = self.paginate_queryset(queryset)
#     #     serializer = self.get_serializer(page, many=True)
#     #     return self.get_paginated_response(serializer.data)

# class VoteAPIView(APIView):
#     def post(self, request, poll_id):
#         poll = Poll.objects.get(id=poll_id)
#         if poll.is_expired():
#             return Response({'error': 'This poll has expired.'}, status=400)
        
#         email = request.data.get('email', None)
#         if not email:
#             return Response({'error': 'Email is required.'}, status=400)

#         # Check if the voter has already voted for this poll
#         if Vote.objects.filter(voter__email=email, poll=poll).exists():
#             return Response({'error': 'You have already voted for this poll.'}, status=400)

#         # Generate and send the OTP via email
#         # ... (implementation of OTP generation and email sending)
#         # ... (store the OTP for validation in the ConfirmVoteAPIView)

#         return Response({'success': 'OTP sent successfully.'}, status=200)

# class ConfirmVoteAPIView(APIView):
#     def post(self, request, poll_id):
#         poll = Poll.objects.get(id=poll_id)
#         if poll.is_expired():
#             return Response({'error': 'This poll has expired.'}, status=400)

#         email = request.data.get('email', None)
#         otp = request.data.get('otp', None)
#         if not email or not otp:
#             return Response({'error': 'Email and OTP are required.'}, status=400)

#         # Validate the OTP
#         # ... (implementation of OTP validation)

#         # Create the vote
#         # ... (implementation of creating the vote)

#         return Response({'success': 'Vote confirmed successfully.'}, status=200)