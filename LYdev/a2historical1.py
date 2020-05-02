import requests
import json
import sys

import searchtweets
from searchtweets import load_credentials
from searchtweets import gen_rule_payload
from searchtweets import ResultStream

from DBprocessor import dbAction

base_url = 'https://api.twitter.com/'
dev_env = 'a2dev'
endpoint = '{}1.1/tweets/search/fullarchive/{}.json'.format(base_url, dev_env)

cdb = dbAction()
db_name = 'historical'

db_inuse = cdb.create_or_get_db(db_name, cdb.dbserver)

search_args = load_credentials("credentials.yaml",
                                yaml_key="search_tweets_api",
                                env_overwrite=False)

print(search_args)

search_param = gen_rule_payload('(Scott Morrison) OR @ScottMorrisonMP', #-37.813740 144.963984
                        results_per_call=50,
                        from_date="2019-10-25",
                        to_date="2019-11-04"
                        )

print (search_param)

if __name__ == "__main__":
    rs = ResultStream(rule_payload=search_param,       
                    max_results=50,
                    **search_args)
    print(rs)

    # stream = rs.stream()
    # r = list(stream)                                                                                                                             
    # print (r)
    try:
        for tw in rs.stream():
            processed = json.loads(json.dumps(tw))
            cdb.insert_raw(processed, db_inuse)
    except:
        print("Error: ", sys.exc_info())

    # with open('testHistorical2.json', 'a+') as f:
    #     for tw in rs.stream():
    #         print (tw)
    #         json.dump(tw, f)
    #         f.write('\n')