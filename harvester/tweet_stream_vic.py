import sys
import json
import requests
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener

import globalvar
from DBprocessor import dbAction
from DataUtils import Analysis
from NLP_core import Sentiment_model as nlp

consumer_key = "zXoReKA7fvCP5CLiC0C2HDI3Y"
consumer_secret = "dpMPUWNgbc9nwq5ntanSx7DFYDWQo7hH51CHxbauX2iKyczH7r"
access_token = "1252534782577086464-9JfCWpydeEfubm8YTbuW0wOFlAjxQz"
access_secret = "aS7HIw8P5AmTRs9gGyFeXPzQsBTQj6JBQTiw2KFyOzSUF"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

class myListener(StreamListener):
    def __init__(self):
        self.dba = dbAction()
        self.dataproc = Analysis()

        self.dbs = self.dba.get_server(self.dba.user, self.dba.pw, ip)
        self.db = self.dba.create_or_get_db(dbname, self.dbs)

    def on_status(self, status):
        if 'Scott Morrison'.lower() in status.text.lower():
            print ("FOUND tweets about PM!!!!!!!!!!!!\n", status.text)
            return True
        
        return False
    
    def on_data(self, data):
        fV = open('data/stream-Victoria.json', 'a')

        tweet = self.dataproc.retain_essential(json.loads(data))
        sentiment = nlp.sentiment_test(tweet['text'], 1)
        tweet['sentiment'] = sentiment
        
        print('\n',tweet['text'])

        # if all attributes are None, don't bother
        if tweet['place'] is None and tweet['user']['location'] is None:
            print('***************SKIP****************')

        #tweet has Place attribute
        elif tweet['place'] is not None and (tweet['place']['country'] == 'AU' or 'Australia' in tweet['place']):

            # if no key words in [place], return
            if not self.dataproc.is_user_in_range(tweet['place']['full_name'], globalvar.all_range):
                print('****************SKIP****************')

            # tweet posted in the state of Victoria
            elif self.dataproc.is_user_in_range(tweet['place']['full_name'], globalvar.wider_range) # elif 'Victoria' in tweet['place']['full_name']:

                # tweet not posted in Melbourne
                if not self.dataproc.is_user_in_range(tweet['place']['full_name'], globalvar.narrower_range):
                    print('\n==========\n',tweet['place']['full_name'], 'Place: From Melbourne\n==========\n')
                    
                    try:
                        msg = dba.insert_raw(tweet, self.db)
                    except:
                        print("Error: ", sys.exc_info())

                    fV.write(json.dumps(tweet)+',\n')
            
            # if no Place attribute available, resort to checking user profile
            elif tweet['user']['location'] is not None:
                
                # skip users with locations not set in VIC
                if self.dataproc.is_user_in_range(tweet['place']['location'], globalvar.all_range):
                    print('****************SKIP****************')

                # Location set as Victoria
                elif self.dataproc.is_user_in_range(tweet['place']['location'], globalvar.wider_range):

                    # user from places in VIC other than Melbourne
                    if not self.dataproc.is_user_in_range(tweet['place']['location'], globalvar.narrower_range):
                        print('\n==========\n',tweet['user']['location'],'\n~~~~~~~~~~User from Melbourne~~~~~~~~~~~~\n')
                        
                        try:
                            msg = dba.insert_raw(tweet, self.db)
                        except:
                            print("Error: ", sys.exc_info())
                        
                        fV.write(json.dumps(tweet)+',\n')
                    #sys.exit('\nExit')

        fV.close()
        return True

    def on_error(self, status_code):
        if status_code == 420:
            print("Error: Rate limit reached")
        print(status_code)
        return True
    
    def on_timeout(self):
        print("Error: Timed out")
        return True

if __name__ == "__main__":

    if len(sys.argv) >= 2:
        ip = sys.argv[1]
        dbname = sys.argv[2]
    else:
        print('Missing parameter(s)')
        sys.exit(0)

    liveStream = Stream(api.auth, myListener())

    while True:
        try:
            liveStream.filter(track=globalvar.track_words_broad)
            # liveStream.filter(locations=[148.057064, -34.780175, 153.268720, -29.548669])
        except Exception as e:
            print(e)
            continue