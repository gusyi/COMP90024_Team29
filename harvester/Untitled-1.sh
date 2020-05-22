curl -X GET http://admin:admin@172.26.132.216:5984/historical-bendigo-raw/_design/count-DDoc/_view/count-view?group=true -o "bendigo_count.json"
curl -X GET http://admin:admin@172.26.132.216:5984/historical-bendigo-raw/_design/senti-DDoc/_view/senti-view?group=true -o "bendigo_sentiment.json"
curl -X GET http://admin:admin@172.26.132.216:5984/historical-ballarat-raw/_design/count-DDoc/_view/count-view?group=true -o "bendigo_count.json"
curl -X GET http://admin:admin@172.26.132.216:5984/historical-ballarat-raw/_design/senti-DDoc/_view/senti-view?group=true -o "bendigo_sentiment.json"