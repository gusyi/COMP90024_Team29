#!/bin/bash

# nohup python3 addto_db.py 172.26.132.216 historical_data/historical-Geelong.json >nohup1.out 2>&1 &
# nohup python3 addto_db.py 172.26.128.114 historical_data/historical-Melbourne.json >nohup2.out 2>&1 &

# nohup python3 addto_db.py 172.26.132.216 ../twitter_sample/Ballarat.json historical-ballarat-raw >nohup1.out 2>&1 &
# nohup python3 addto_db.py 172.26.128.114 ../twitter_sample/Bendigo.json historical-bendigo-raw >nohup2.out 2>&1 &
# nohup python3 addto_db.py 172.26.134.61 ../twitter_sample/Melton.json historical-melton-raw >nohup3.out 2>&1 &
nohup python3 addto_db.py 172.26.132.216 ../twitter_sample/Geelong.json historical-ballarat-raw >nohup4.out 2>&1 &
nohup python3 addto_db.py 172.26.128.114 ../twitter_sample/Victoria.json historical-victoria-raw >nohup6.out 2>&1 &
# nohup python3 addto_db.py 172.26.134.61 data/historical-melbourne.json historical-melbourne-raw >nohup7.out 2>&1 &



# . ../deployment/ansible/openrc.sh; ansible-playbook -i ../deployment/ansible/inventory/hosts --private-key=~/.ssh/team29.pem --ask-become-pass movetocloud.yml -vv