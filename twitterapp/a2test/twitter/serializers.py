from rest_framework import serializers
from twitter.models import Tweet

# Lead Serializer
class TweetSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tweet
    fields = '__all__'