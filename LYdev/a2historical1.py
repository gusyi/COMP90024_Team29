import requests
import base64
import json
import searchtweets
from searchtweets import load_credentials
from searchtweets import gen_rule_payload
from searchtweets import ResultStream

base_url = 'https://api.twitter.com/'
dev_env = 'a2dev'
endpoint = '{}1.1/tweets/search/fullarchive/{}.json'.format(base_url, dev_env)

search_args = load_credentials("credentials.yaml",
                                yaml_key="search_tweets_api",
                                env_overwrite=False)

print(search_args)

search_param = gen_rule_payload("Scott Morrison", 
                        results_per_call=100,
                        from_date="2019-10-25 07:15",
                        to_date="2019-11-04 23:11"
                        )

rs = ResultStream(rule_payload=search_param,
                  max_results=100,
                  **search_args)
print(rs)

with open('testHistorical.json', 'a+') as f:
    for tw in rs.stream():
        print (tw)
        json.dump(tw, f)
        f.write('\n')

