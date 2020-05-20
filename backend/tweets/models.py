from django.db import models

class TweetTestData(models.Model):
    text = models.CharField(max_length = 200,blank=True,null=False)
    userid = models.CharField(max_length = 20)
    hashtags = models.CharField(max_length = 200,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    geolocation = models.CharField(max_length=20)
    sentiment_tag = models.CharField(max_length=20, blank=True, null=True)


class TweetResultData(models.Model):
    date = models.DateField(null = False)
    tweetcounts = models.IntegerField()
    location = models.CharField(max_length=30, blank=True)
    approval_rate = models.DecimalField(max_digits=6, decimal_places=5)
    city_id = models.CharField(max_length =30, null = False, default = "Melbourne")









