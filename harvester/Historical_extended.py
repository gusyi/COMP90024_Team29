import sys
import json
from datetime import date, datetime
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

# def probe_timeline(collection):
#     for item in collection:
#         item = json.loads(json.dumps(item._json))

#         if dataproc.get_create_date(item) < end_date: #don't care anything posted beyond the cut-off date
#             break
            
#         if dataproc.contains_keywords(item):
#             tweet_count1 += 1
#             print(tl['text'],'\n-----------------------\n')

#             if dataproc.is_retweet(item):
#                 print('!!! Found RT !!!')
#                 source_id = dataproc.get_source_tweet(tl)
#                 rts = api_rt.retweeters(id=source_id,stringify_ids=True)

#                 print('Retweeter count...', len(rts))

def add_to_db(data, dbname):
    fM = open('Melbourne1.json', 'a+')
    try:
        msg = db.insert_raw(data, dbname)
    except:
        print("Error: ", sys.exc_info())
    
    if msg == "Success":
        fM.write(json.dumps(data)+',\n')

def main():
    base = 'historical-melbourne'
    hismel = globalvar.app_assignment[base]
    api_base = get_api(hismel)
    db_base = db.create_or_get_db('historical-melbourne2', db.dbserver)

    timeline = 'historical-timeline'
    histl = globalvar.app_assignment[timeline]
    api_tl = get_api(histl)
    db_tl = db.create_or_get_db(timeline, db.dbserver)

    retweet = 'historical-retweet'
    hisrt = globalvar.app_assignment[retweet]
    api_rt = get_api(hisrt)
    db_rt = db.create_or_get_db(retweet, db.dbserver)

    end_date = date(2019, 11, 1) #cut-off date

    c=0
    lvl0 = tweepy.Cursor(api_base.search, q=globalvar.search_terms, 
                            until='2020-05-05', #7 days of data including 5/5
                            geocode='-37.812279,144.962270,35km', #35km radius of Mel CBD
                            lang='en', #include emoji?
                            tweet_mode='extended').items()

    for t in lvl0:
        add_to_db(t._json, db_base)

        c +=1
        print ('++++++++++++++++ NUMBER ++++++++++++++++++', c)

        userid = dataproc.get_user_id(t)
        print('Probing user...', userid)

        tweet_count1 = 0
        tweet_count2 = 0
        lvl1TL = tweepy.Cursor(api_tl.user_timeline, user_id=userid).items()
        for tw in lvl1TL:
            if dataproc.get_create_date(tw.created_at) < end_date: #don't care anything posted beyond the cut-off date
                break
            
            if dataproc.contains_keywords(tw.text):
                tweet_count1 += 1
                print(tw.text,'\n-----------------------\n')

                add_to_db(tw._json, db_base)

                if dataproc.is_retweet(tw._json):
                    print('!!! Found RT !!!')
                    source_id = dataproc.get_source_tweet(tw._json)
                    rts = api_rt.retweeters(id=source_id,stringify_ids=True)

                    print('Retweeter count...', len(rts))

                    rt_profiles = api_rt.lookup_users(user_ids=rts)
                         
                    for profile in rt_profiles:
                        if dataproc.is_user_in_range(profile.location, globalvar.narrower_range):
                            print ('User {} in MEL...........'.format(profile.id_str))
                            lvl2TL = tweepy.Cursor(api_tl.user_timeline, user_id=profile.id_str).items()

                            for tl in lvl2TL:
                                if dataproc.get_create_date(tl.created_at) < end_date: #don't care anything posted beyond the cut-off date
                                    break
                
                                if dataproc.contains_keywords(tl.text):
                                    tweet_count2 += 1
                                    print(tl.text,'\n************************\n')
                                    
                                    add_to_db(tl._json, db_base)

                            print(tweet_count2)

        print(tweet_count1)

if __name__ == '__main__':
    main()