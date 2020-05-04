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
        print('\n',tweet['text'])

        if tweet['place'] is None and tweet['user']['location'] is None:
            return True;
        
        if tweet['place'] is not None and tweet['place']['country'] == 'AU':

            # if no key words in [place], pass to the next part
            if 'Victoria'  not in tweet['place']['full_name'] and \
               'Melbourne' not in tweet['place']['full_name']:
                print('\nNO==NO==NO\n',tweet['place']['full_name'], '\nNO==NO==NO\n')

            elif tweet['place']['country_code'] == 'AU' and \
                 'Victoria' in tweet['place']['full_name']:
                # if from Melbourne, categorize 
                if 'Melbourne' or 'Mel' in tweet['place']['full_name']:
                    print('\n==========\n',tweet['place']['full_name'], \
                        'Place: It is from Melbourne\n==========\n')
                # else it is from other places in Vic
                else:
                    print('\n==========\n',tweet['place']['full_name'], \
                        'Place: It is from other places in Vic\n==========\n')

                f.write(json.dumps(tweet))
                sys.exit('\nExit')

            # it may from Melbourne
            elif tweet['place']['country_code'] == 'AU' and \
            'Melbourne' in tweet['place']['full_name']:
                print('\n==========\n',tweet['place']['full_name'], \
                  'It is from Melbourne\n==========\n')
                f.write(json.dumps(tweet))
                sys.exit('\nExit')

        elif tweet['user']['location'] is not None:

            if 'Victoria'  not in tweet['user']['location'] and \
               'Melbourne' not in tweet['user']['location']:
               print('\nNO==NO==NO\n', tweet['user']['location'], '\nNO==NO==NO\n')

            elif 'Victoria' in tweet['user']['location']:

                # if from Melbourne, categorize 
                if 'Melbourne' or 'Mel' in tweet['user']['location']:
                    print('\n==========\n',tweet['user']['location'], \
                        '\n1. It is from Melbourne\n==========\n')
                else:
                    print('\n==========\n',tweet['user']['location'], \
                        '\nIt is from other places in Vic\n==========\n')
                f.write(json.dumps(tweet))
                sys.exit('\nExit')

            elif 'Melbourne' in tweet['user']['location']:
                print('\n==========\n',tweet['user']['location'], \
                  '\n2. It is from Melbourne\n==========\n')
                f.write(json.dumps(tweet))
                sys.exit('\nExit')

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