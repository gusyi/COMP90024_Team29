from rest_framework import serializers
from tweets.models import TweetTestData

#Tweetter serializer

class TweetTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TweetTestData
        fields = '__all__'