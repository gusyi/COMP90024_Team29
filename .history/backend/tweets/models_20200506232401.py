from django.db import models
from couchdb.mapping import Document, TextField, DateTimeField, ListField


class TweetData(Document):
    text = TextField()
    userid = TextField()
    hashtags = ListField(TextField)
    date = DateTimeField()
    geolacation = ListField(TextField)

class Question(models.Model):
    text = models.CharField(max_length=100)
    


