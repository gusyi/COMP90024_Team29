from django.db import models
from couchdb.mapping import Document, TextField, DateTimeField, ListField


class TweetData(Document):
    tweetid = TextField()
    text = TextField()
    userid = TextField()
    hashtags = ListField(TextField)
    created_at = DateTimeField()
    geolocation = ListField(TextField)
    city = TextField()

class TweetTestData(models.Model):
    tweetid = models.CharField(max_length = 40, default='000000')
    text = models.CharField(max_length = 200,blank=True,null=False)
    userid = models.CharField(max_length = 20, default='000000')
    hashtags = models.CharField(max_length = 200,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    geolocation = models.CharField(max_length=20)
    sentiment_tag = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length = 30, null=True)





