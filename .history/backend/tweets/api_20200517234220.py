from tweets.models import TweetTestData,TweetResultData
from rest_framework import viewsets, permissions
from .serializers import TweetTestSerializer, TweetResultSerializer

# TweetTestData Viewset
class TweetTestViewSet(viewsets.ModelViewSet):
    queryset = TweetTestData.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class = TweetTestSerializer

class TweetResultViewSet(viewsets.ModelViewSet):
    queryset = TweetResultData.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class = TweetResultSerializer
