import json
import pandas as pd
from tweets.models import TweetResultData, City

def run():
    FILE_NAME = 'mapreduce_result/bendigo.json'
    f = open(FILE_NAME, 'r',encoding = "utf-8") 
    data_df = pd.DataFrame()
    date = []
    tweetcounts = []
    approval_rate = []
    with open(FILE_NAME) as json_file:
        data = json.load(json_file)
        for row in  data["daily_sentiment"]["rows"]:
            date.append(row['key'][0])
            tweetcounts.append(int(row['value'] / row['ratio']))
            approval_rate.append(row['ratio'])
    bendigo_df['date'] = date
    bendigo_df['tweetcounts'] = tweetcounts
    bendigo_df['approval_rate'] = approval_rate

    bendigo_df.head()