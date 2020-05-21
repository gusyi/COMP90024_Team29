from django.db import models

class TweetTestData(models.Model):
    text = models.CharField(max_length = 200,blank=True,null=False)
    userid = models.CharField(max_length = 20)
    hashtags = models.CharField(max_length = 200,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    geolocation = models.CharField(max_length=20)
    sentiment_tag = models.CharField(max_length=20, blank=True, null=True)


class City (models.Model):
    name = models.CharField(max_length=30, blank=False, null=False, default="Melbourne")
    average_income = models.IntegerField()
    education_level = models.CharField(max_length=50, blank=True)
    migration_percentage = models.DecimalField(max_digits=6, decimal_places=3)
    migration_number = models.IntegerField(null = True, blank=True, default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class TweetResultData(models.Model):
    date = models.DateField(null = False)
    tweetcounts = models.IntegerField()
    approval_rate = models.DecimalField(max_digits=6, decimal_places=5, help_text='decimal, 0-1')
    cityname = models.CharField(max_length=30, blank=False, null=False, default="Melbourne",
                                choices=[('Melbourne', ('Melbourne')), 
                                        ('Geelong', ('Geelong')), 
                                        ('Ballarat', ('Ballarat')), 
                                        ('Bendigo', ('Bendigo')),
                                        ('Melton', ('Melton'))])
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        ordering = ['date', 'city']









