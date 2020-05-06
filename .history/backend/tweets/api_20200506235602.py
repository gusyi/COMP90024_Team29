from .models import TweetTestData
from rest_framework import viewsets, permissions
from .serializers import TweetTestSerializer

# TweetTestData Viewset
class LeadViewSet(viewsets.ModelViewSet):
    queryset = TweetTestData.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class = TweetTestSerializer