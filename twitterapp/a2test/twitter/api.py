from twitter.models import Tweet
from rest_framework import viewsets, permissions
from .serializers import TweetSerializer

# Tweet Viewset
class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class = TweetSerializer