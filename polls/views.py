from rest_framework import generics, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from . models import Poll
from .serializers import ListPollSerializer
from .paginations import PollsListPagination
from .filters import PollsListFilter

class PollListAPIView(generics.ListAPIView):
    """
    Poll list pages of data for poll.
    """
    serializer_class = ListPollSerializer
    queryset = Poll.objects.order_by('-expiry_date')
    permission_classes = [permissions.AllowAny]
    pagination_class = PollsListPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = PollsListFilter
