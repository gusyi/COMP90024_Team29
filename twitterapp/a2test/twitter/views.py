from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from twitter.models import Tweet, SERVER
from twitter.serializers import TweetSerializer

db = SERVER['test']

@api_view(['POST'])
def create_paper(request):
    data = JSONParser().parse(request)

    serializer = TweetSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def tweet_detail(request, tid):
    tweet = Tweet.load(db, tid)
    serializer = TweetSerializer(paper)
    return Response(serializer.data)