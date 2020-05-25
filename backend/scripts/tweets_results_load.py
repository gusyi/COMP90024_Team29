import json
import pandas as pd
from tweets.models import TweetResultData, City

def run():
    TweetResultData.objects.all().delete()
    city_names = ["Ballarat","Melbourne","Geelong","Bendigo"]
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
