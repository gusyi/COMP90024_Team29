from __future__ import absolute_import, print_function

from tweepy import OAuthHandler, Stream, StreamListener

import json
import sys

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="zXoReKA7fvCP5CLiC0C2HDI3Y"
consumer_secret="dpMPUWNgbc9nwq5ntanSx7DFYDWQo7hH51CHxbauX2iKyczH7r"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="1252534782577086464-9JfCWpydeEfubm8YTbuW0wOFlAjxQz"
access_token_secret="aS7HIw8P5AmTRs9gGyFeXPzQsBTQj6JBQTiw2KFyOzSUF"

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):

        f = open('test.json', 'w')

        tweet = json.loads(data)
        print(tweet['text'])

        if tweet['place'] is not None and tweet['place']['country_code'] == 'AU':
            print('\n#########')
            print(tweet['place'])
            f.write(json.dumps(tweet))
            sys.exit('It has place\n#########\n')
        else:
            if tweet['user']['location'] is not None and \
                ('Vic' in tweet['user']['location'] or \
                'Melbourne' in tweet['user']['location']):

                print('\n#########')
                print(tweet['user']['location'])
                print('It is in Vic\n#########\n')
                #sys.exit('\n It is in Vic\n')

            elif tweet['user']['location'] is not None:
                print('\n',tweet['user']['location'],'\n')
            else:
                print("not")

        f.close()
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['Scott Morrison, Morrison, @ScottMorrisonMP'])
    #stream.filter(track=['@realDonaldTrump, Donald Trump'])