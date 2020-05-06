from django.db import models
from couchdb.mapping import Document, TextField, DateTimeField, ListField


class TweetData(Document):
    text = TextField()
    userid = TextField()
    hashtags = ListField(TextField)
    date = DateTimeField()
    geolacation = ListField(TextField)

class TweetTestData(models.Model):
    text = models.TextField(max_length=200,blank=True,null=False)
    userid = models.CharField(max_length = 20)
    hashtags = models.ListField(blank=True)
    date = models.DateTimeField()
    geolocation = models.CharField(max_length=20)
    sentiment_tag = models.CharField(max_length=20, blank=True, null=True)





