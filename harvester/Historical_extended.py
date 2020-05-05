import sys
import json
from datetime import date
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener

import globalvar
from DBprocessor import dbAction
from DataUtils import Analysis

db = dbAction()
dataproc = Analysis()

def get_api(assigned_app):
    consumer_key = globalvar.app_credentials[assigned_app]['consumer_key']
    consumer_secret = globalvar.app_credentials[assigned_app]['consumer_secret']
    auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
    # auth.set_access_token(access_token, access_secret)

    return tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def main():
    base = 'historical-melbourne'
    hismel = globalvar.app_assignment[base]
    api_base = get_api(hismel)
    db_base = db.create_or_get_db(base, db.dbserver)

    expansion = 'historical-potential'
    hisexp = globalvar.app_assignment[base]
    api_exp = get_api(hisexp)
    db_exp = db.create_or_get_db(expansion, db.dbserver)

    end_date = date(2019, 11, 1) #cut-off date
    for t in tweepy.Cursor(api_base.search, q=globalvar.search_terms, 
                            until='2020-05-05', #7 days of data including 5/5
                            geocode='-37.80,145.11,75km', #75km radius of Mel center
                            lang='en', #include emoji?
                            tweet_mode='extended').items():
        t = json.loads(json.dumps(t._json))
        try:
            db.insert_raw(t, db_base)
        except:
            print("Error: ", sys.exc_info())

        userid = dataproc.get_user_id(t)
        print('Probing user...', userid)

        tweet_count = 0
        for tl in tweepy.Cursor(api_exp.user_timeline, user_id=userid).items():
            tl = json.loads(json.dumps(tl._json))
            
            if dataproc.get_create_date(tl) < end_date: #don't care anything posted beyond the cut-off date
                break
            
            if dataproc.contains_keywords(tl):
                tweet_count += 1
                print(tl['text'],'\n-----------------------\n')

        print(tweet_count)

        break




# rtcount = 0
# viccount = 0
# for doc in doclist:
#     doc = json.loads(json.dumps(doc))
#     if 'retweeted_status' in doc:
#         source_id = dataproc.get_source_tweet(doc)
#         retweets = api.retweets(source_id)
#         rtcount = rtcount + len(retweets)

#         for r in retweets:
#             r = json.loads(json.dumps(r._json))
#             if dataproc.geo_in_range(r):
#                 viccount = viccount+1
#                 try:
#                     db.insert_raw(r, db_inuse)
#                 except:
#                     print("Error: ", sys.exc_info())
#             else:
#                 print(r['id_str'], "not in range")

# # source_id = dataproc.get_source_tweet(l[0])
# # print (source_id)
# # results = api.retweets(source_id)
# # print(len(results))

# print(rtcount)
# print(viccount)

if __name__ == '__main__':
    main()