from django.urls import path
from . views import PollListAPIView
urlpatterns = [
    path('list-polls-pages/', PollListAPIView.as_view(), name = 'list-polls-pages')
]