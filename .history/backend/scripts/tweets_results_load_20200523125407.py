import json
import pandas as pd
from tweets.models import TweetResultData, City

"""
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


"""

def run():
    #TweetResultData.objects.all().delete()
    city_names = ["Geelong"]
    for city_name in city_names:

        FILE_NAME = 'mapreduce_result/'+city_name+'.json'

        with open(FILE_NAME) as json_file:
            data = json.load(json_file)
            rowindex = 0
            for row in  data["daily_sentiment"]["rows"]:
                print(row)
                c, created = City.objects.get_or_create(name = city_name)
                if row['ratio'] == 0:
                    tweetcount = data["daily_total"][row['key'][0]]
                else:
                    tweetcount = int(row['value'] / row['ratio'])

                result = TweetResultData(
                    date = row['key'][0],
                    tweetcounts = tweetcount,
                    approval_rate = row['ratio'],
                    cityname = city_name,
                    city = c
                )
                result.save()
