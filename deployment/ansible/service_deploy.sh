#!/bin/bash

. ./openrc.sh; ansible-playbook -i ./inventory/hosts --private-key=~/.ssh/team29.pem --ask-become-pass service_deploy.yml -vv