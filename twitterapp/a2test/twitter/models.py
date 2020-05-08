from django.db import models

from django.conf import settings
from couchdb import Server
from couchdb.mapping import Document, TextField

#set up connection to DB
SERVER = Server(getattr(settings, 'COUCHDB_SERVER', 'http://127.0.0.1:5984'))
if 'test' not in SERVER:
    SERVER.create('test')


class Tweet(models.Model):
    tid = models.CharField(max_length=40, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    userid = models.CharField(max_length=40)
    text = models.CharField(max_length=400)
    city = models.CharField(max_length=40, blank=True)
    geoinfo = models.CharField(max_length=80, blank=True)
    hashtags = models.CharField(max_length = 200, blank=True)
    sentiment_tag = models.CharField(max_length=20, blank=True, null=True)