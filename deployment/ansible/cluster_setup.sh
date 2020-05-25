#!/bin/bash

. ./openrc.sh; ansible-playbook -i ./inventory/hosts --private-key=~/.ssh/team29.pem --ask-become-pass cluster_setup.yml -v