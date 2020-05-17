from rest_framework import serializers
from tweets.models import TweetTestData,TweetResultData

#Tweetter serializer

class TweetTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TweetTestData
        fields = '__all__'

class TweetResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TweetTestData
        fields = '__all__'