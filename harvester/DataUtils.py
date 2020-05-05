import json
import re
from datetime import datetime, timezone

import globalvar

class Analysis:
    # vic metro [144.593742, -38.433859], [144.593742, -37.511274], [145.512529, -37.511274], [145.512529, -38.433859]
    # vic greater [[140.961682, -39.15919],[140.961682, -33.980426], [149.976679, -33.980426], [149.976679, -39.15919]]
    # act [[148.995922,-35.480260],[148.995922,-35.147699],[149.263643,-35.147699],[149.263643,-35.480260]]
    # nsw metro [[150.520929, -34.118347], [150.520929, -33.578141], [151.343021, -33.578141], [151.343021, -34.118347]]
    def get_user_id(self, tweet):
        return tweet['user']['id_str']
    
    def get_create_date(self, tweet):
        fulltimestamp = datetime.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y').replace(tzinfo=timezone.utc)
        return fulltimestamp.date()
    
    def geo_in_range(self, tweet): #coord=tweet['place']['bounding_box']['coordinates'][0]
        if not tweet['place'] is None:
            coord = tweet['place']['bounding_box']['coordinates']
            plname = tweet['place']['name']
            if coord[0][0] >= 140.961682 and coord[1][1] <= -33.980426 and coord[2][1] <= 149.976679 and coord[3][2] >= -39.15919 \
                and not plname in ['Canberra', 'Sydney', 'New South Wales']:
                return True

        else:
            if not tweet['user']['location'] is None:
                loc = tweet['user']['location'].lower()
                if 'victoria'.lower() in loc or 'Melbourne'.lower() in loc or 'VIC'.lower() in loc:
                    return True
        
        return False
    
    def is_melb(self, tweet):
        pass
    
    def get_source_tweet(self, tweet):
        return tweet['retweeted_status']['id_str']
    
    def contains_keywords(self, tweet):
        if any(word in tweet['text'] for word in globalvar.track_words):
            return True

    # def get_sentiment(self, text):
    #     tb = TextBlob(text)
    #     sen = tb.sentiment

    #     return sen.polarity, sen.subjectivity
