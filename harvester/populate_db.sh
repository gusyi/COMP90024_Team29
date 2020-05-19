#!/bin/bash

nohup python3 addto_db.py 172.26.132.216 historical_data/historical-Geelong.json >nohup1.out 2>&1 &
nohup python3 addto_db.py 172.26.128.114 historical_data/historical-Melbourne.json >nohup2.out 2>&1 &

# . ../deployment/ansible/openrc.sh; ansible-playbook -i ../deployment/ansible/inventory/hosts --private-key=~/.ssh/team29.pem --ask-become-pass movetocloud.yml -vv