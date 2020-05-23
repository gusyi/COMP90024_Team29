import sys
import json
import couchdb

import globalvar
from NLP_core import Sentiment_model as nlp
from DBprocessor import dbAction
from DataUtils import Analysis

if __name__ == '__main__':
    dba = dbAction()
    dataproc = Analysis()

    # #------test purpose only------
    # fname = 'historical_data/historical-Geelong.json'
    # print ((fname.lower().split('/')[1]).split('.')[0] + '-raw')
    # #------test purpose only------

    if len(sys.argv) >= 3:
        ip = sys.argv[1]
        fname = sys.argv[2]
        dbname = sys.argv[3]
    else:
        print('Missing parameter(s)')
        sys.exit(0)

    # dbname = (fname.lower().split('/')[1]).split('.')[0] + '-raw'

    dbserver = dba.get_server(dba.user, dba.pw, ip)
    db = dba.create_or_get_db(dbname, dbserver)

    #cleanse raw data line by line
    with open(fname, encoding='utf-8') as f:
        # #------test purpose only------
        # count = 0
        # #------test purpose only------
        for line in f:
            line = line.strip(',\n')
            # print (line)
            tweet = json.loads(line)
            print (type(tweet))
            if 'full_text' not in tweet:
                sentiment = nlp.sentiment_test(tweet['text'], 1)
            else:
                sentiment = nlp.sentiment_test(tweet['full_text'], 1)

            doc = dataproc.retain_essential(tweet)
            doc['sentiment'] = sentiment
            print(doc)
            try:
                msg = dba.insert_cleansed(doc, db)
            except:
                print("Error: ", sys.exc_info())

